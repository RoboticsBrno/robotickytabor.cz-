import os
from PIL import Image
from PIL.ExifTags import TAGS


def get_date_taken(path):
    try:
        image = Image.open(path)
        exif_data = image._getexif()
        for tag, value in exif_data.items():
            decoded_tag = TAGS.get(tag, tag)
            if decoded_tag == "DateTimeOriginal":
                return value
    except Exception as e:
        print(f"Error getting date from {path}: {e}")
    return None


def resize_image(image_path, output_path, max_size):
    img = Image.open(image_path)
    img.thumbnail((max_size, max_size), Image.LANCZOS)
    img.save(output_path, "JPEG")


def process_images(input_folder, img_output_folder, thumb_output_folder, prefix):
    if not os.path.exists(img_output_folder):
        os.makedirs(img_output_folder)
        print(f"Created output folder: {img_output_folder}")

    if not os.path.exists(thumb_output_folder):
        os.makedirs(thumb_output_folder)
        print(f"Created thumbnail folder: {thumb_output_folder}")

    images_info = []
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ):
            file_path = os.path.join(input_folder, filename)
            date_taken = get_date_taken(file_path)
            if date_taken:
                images_info.append((date_taken, file_path))

    images_info.sort()  # Sort by date_taken, oldest first

    index = 1
    processed_images = []
    for date_taken, file_path in images_info:
        base_name = f"{prefix}-{index:04d}.jpg"
        img_output_path = os.path.join(img_output_folder, base_name)
        thumb_output_path = os.path.join(thumb_output_folder, base_name)

        # Resize for normal image (max 1500)
        resize_image(file_path, img_output_path, 1500)
        print(f"Processed normal image: {img_output_path}")

        # Resize for thumbnail (max 500)
        resize_image(file_path, thumb_output_path, 500)
        print(f"Processed thumbnail: {thumb_output_path}")

        processed_images.append(base_name)
        index += 1

    return processed_images


def generate_html(
    images_info, output_html_path, year, img_output_folder, thumb_output_folder
):
    section_template = """
<section id="{year}">
    <div id="container">
        <h2 class="text-black-50 text-center">{year}</h2>
        <ul class="js--dynamic-place-{year}">
{main_items}
        </ul>
        <button class="js--add-dynamic-{year} btn">Zobrazit více</button>
    </div>
</section>

<ul class="js--dynamic-items-{year} is-hidden">
{hidden_items}
</ul>

<script>
$('.js--add-dynamic-{year}').on('click', function (e) {{
    e.preventDefault();
    var items = $('.js--dynamic-items-{year}');
    instanceH.addToImageLightbox(items.find('a'));
    $('.js--dynamic-place-{year}').append(items.find('li').detach());
    $(this).remove();
    items.remove();
}});
</script>
"""
    main_items = ""
    hidden_items = ""
    for i, image in enumerate(images_info):
        img_path = os.path.join(img_output_folder, image)
        thumb_path = os.path.join(thumb_output_folder, image)
        list_item = f'            <li><a href="{img_path}" data-imagelightbox="h"><img src="{thumb_path}" alt=" " loading="lazy"/></a></li>'
        if i < 5:
            main_items += list_item + "\n"
        else:
            hidden_items += list_item + "\n"

    html_content = section_template.format(
        year=year, main_items=main_items, hidden_items=hidden_items
    )

    with open(output_html_path, "w") as html_file:
        html_file.write(html_content)
    print(f"Generated HTML file: {output_html_path}")


if __name__ == "__main__":
    year = "2024"
    input_folder = f"original/{year}"
    img_output_folder = f"img/{year}"
    thumb_output_folder = f"thumb/{year}"
    prefix = f"RoboCamp-{year}"
    output_html_path = "generateGallery.html"

    print(f"Starting processing images for the year {year}...")
    images_info = process_images(
        input_folder, img_output_folder, thumb_output_folder, prefix
    )
    generate_html(
        images_info, output_html_path, year, img_output_folder, thumb_output_folder
    )
    print("Processing completed.")
