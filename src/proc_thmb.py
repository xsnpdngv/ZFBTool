from PIL import Image, ImageDraw, ImageFont


def crop_to_resolution(image_path, target_width, target_height):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the original image
    orig_width, orig_height = img.size

    # Calculate how what to crop to keep the top-right corner
    top = 0
    right = orig_width
    left = max(orig_width - target_width, 0)
    bottom = min(orig_height, target_height)

    # Crop the image
    cropped_image = img.crop((left, top, right, bottom))

    return cropped_image


def crop(img, new_width, new_height, start_point='top-right'):
    """
    :param img: Pillow image object given back by PIL.Image.open
    :param start_point: either 'top-left', 'top-right', 'bottom-left' or 'bottom-right'

    Example usage:

        img = Image.open("sample_img.png")
        cropped_img = crop(img_path, target_width=144, target_height=208, 'top-right')
        cropped_img.show()  # To display the cropped image
        cropped_img.save("cropped_img.png")  # To save the cropped image
    """

    # Get the size of the original image
    width, height = img.size

    # Calculate the rectangular to crop
    if 'center' == start_point:
        top = (height - new_height) // 2    if height - new_height > 0    else 0
        bottom = height // 2 + (height - new_height) // 2    if height - new_height > 0    else height
        left = (width - new_width) // 2    if width - new_width > 0    else 0
        right = width // 2 + (width - new_width) // 2    if width - new_width > 0    else width
    else:
        top = 0
        left = 0
        bottom = height
        right = width
        if 'top' in start_point:
            bottom = min(height, new_height)
        if 'bottom' in start_point:
            top = height - new_height    if height - new_height > 0    else 0
        if 'left' in start_point:
            right = min(width, new_width)
        if 'right' in start_point:
            left = width - new_width    if width - new_width > 0    else 0

    return img.crop((left, top, right, bottom))


def add_text(img, text, position=(7, 0), font_path=None, font_size=20, font_color=(0, 0, 0), outline_color=(255, 255, 255), outline_width=2):
    """
    :param img: Pillow image object given back by PIL.Image.open

    Example usage:

        img = Image.open("sample_img.png")
        img_with_text = add_text(img, text="ASDF",
                                 #position=(7, 0),
                                 font_path='../assets/Lalezar-Regular.ttf',
                                 #font_size=20,
                                 font_color=(255,255,255),
                                 #outline_color=GBA_COLOR,
                                 outline_color=(0,0,0),
                                 outline_width=1
                                 )
        img_with_text.show()  # To display the cropped image
        img_with_text.save("img_with_text.png")
    """

    draw = ImageDraw.Draw(img)
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    # Draw outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            draw.text((position[0] + dx, position[1] + dy), text, fill=outline_color, font=font)

    # Draw text over outline
    draw.text(position, text, fill=font_color, font=font)

    return img




