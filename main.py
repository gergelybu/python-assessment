import json
from slides import Slide
from pptx import Presentation
from pptx.util import Inches

def create_title_slide(slide, title, content):
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

def create_text_slide(slide, title, content):
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

def create_list_slide(slide, title, items):
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

def create_picture_slide(slide, title, image_filename):
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

def create_plot_slide(slide, title, data, config):
    slide.shapes.title.text = title
    slide.placeholders[1].text = content

def create_presentation(slides):
    presentation = Presentation()

    for slide_data in slides:
        slide_type = slide_data.slide_type
        slide_title = slide_data.title
        slide_content = slide_data.content

    if slide_type == 'title':
        slide = presentation.slides.add_slide(presentation.slide_layouts[0])
        create_title_slide(slide, slide_title, slide_content)
    elif slide_type == 'text':
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        create_text_slide(slide, slide_title, slide_content)
    elif slide_type == 'list':
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        create_list_slide(slide, slide_title, slide_content)
    elif slide_type == 'picture':
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        create_picture_slide(slide, slide_title, slide_content)
    elif slide_type == 'plot':
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        create_plot_slide(slide, slide_title, slide_content, slide_data.configuration)

    return presentation


# Asking for the configuration file from the user
json_file_path = input("Enter the path to the configuration file: ")

with open(json_file_path) as json_file:
    json_data = json.load(json_file)

slides = []
for slide_data in json_data['presentation']:
    slide_type = slide_data['type']
    slide_title = slide_data['title']
    slide_content = slide_data['content']
    configuration = slide_data.get('configuration', None)
    slide = Slide(slide_type, slide_title, slide_content, configuration)
    slides.append(slide)

presentation = create_presentation(slides)

output_file_path = input("Enter the path to save the presentation: ")

presentation.save(output_file_path)