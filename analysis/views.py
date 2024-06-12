import matplotlib.pyplot as plt
import io
import pandas as pd
import base64
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'analysis/success.html')
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('media/temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def plot_histogram(request):
    # Load the data
    data = pd.read_csv('media/temp.csv')

    # Generate histograms for numeric columns
    numeric_columns = data.select_dtypes(include='number').columns
    num_columns = len(numeric_columns)

    if num_columns == 0:
        return HttpResponse("No numeric columns found in the uploaded CSV file.", content_type='text/plain')

    fig, axes = plt.subplots(num_columns, 1, figsize=(8, 4 * num_columns))

    if num_columns == 1:
        axes = [axes]  # Ensure axes is iterable

    for ax, column in zip(axes, numeric_columns):
        ax.hist(data[column].dropna(), bins=20, alpha=0.75)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')

    plt.tight_layout()

    # Convert plot to image and encode as base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    histogram_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Prepare data for the template
    head_data = data.head().to_html(classes='table table-striped')
    summary_stats = data.describe().to_html(classes='table table-striped')
    missing_values = data.isnull().sum().to_frame(name='Missing Values').to_html(classes='table table-striped')

    context = {
        'histogram_image': histogram_image,
        'head_data': head_data,
        'summary_stats': summary_stats,
        'missing_values': missing_values

    }

    return render(request, 'analysis/results.html', context)
