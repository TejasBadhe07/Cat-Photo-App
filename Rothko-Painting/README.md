# Rothko-Painting

Every HTML element is its own box – with its own spacing and a border. This is called the Box Model.
In this project, you'll see how to use CSS and the Box Model to create your own Rothko-style rectangular art pieces.

In the CSS box model, every HTML element is treated as a box with four areas.

Imagine you receive a box from your favorite online retailer -- the content is the item in the box, or in our case, a header, paragraph, or image element

The content is surrounded by a space called padding, similar to how bubble wrap separates an item from the box around it.

Think of the border like the cardboard box your item was shipped in.

Margin is the area outside of the box, and can be used to control the space between other boxes or elements.

Even though your <div> has no text, it's still treated as a box with content. Write a CSS rule that uses the .canvas class selector and set its width to 500 pixels. Here's a CSS rule that sets the width of the class card to 300 pixels:

.card {
  width: 300px;
}

The colors and shapes of your painting are too sharp to pass as a Rothko.

Use the filter property to blur the painting by 2px in the .canvas element.

Here's an example of a rule that add a 3px blur:

p {
  filter: blur(3px);
}

The rectangles are too small and their edges don't have the soft quality of a painting.

Increase the area and soften the edges of .one by setting its box-shadow to 0 0 3px 3px #efb762.
The corners of each rectangle are still too sharp.

Round each corner of the element by 9 pixels, using the border-radius property.
The border-radius property accepts up to four values to round the top-left, top-right, bottom-right, and bottom-left corners.