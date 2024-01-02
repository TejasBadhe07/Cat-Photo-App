# Typography by building Nutrition Label

Typography is the art of styling your text to be easily readable and suit its purpose.

In this course, you'll use typography to build a nutrition label webpage. You'll learn how to style text, adjust line height, and position your text using CSS.

Within your head element, add a link element with the rel attribute set to stylesheet and the href attribute set to https://fonts.googleapis.com/css?family=Open+Sans:400,700,800.

This will import the Open Sans font family, with the font weight values 400, 700, and 800.
Create a body selector and give it a font-family set to Open Sans with a fallback of sans-serif.

Remember that fonts with spaces in the name must be wrapped in quotes for CSS.

Good use of white space can bring focus to the important elements of your page, and help guide your user's eyes through your text.

Give your .label selector a width property set to 270px.
If you inspect your .label element with your browser's developer tools, you may notice that it's actually 288 pixels wide instead of 270. This is because, by default, the browser includes the border and padding when determining an element's size.

To solve this, reset the box model by creating a * selector and giving it a box-sizing property of border-box.
Remember that the use of h1, h2, and similar tags determine the semantic structure of your HTML. However, you can adjust the CSS of these elements to control the visual flow and hierarchy.

Create an h1 rule and set the font-weight property to 800. This will make your h1 text bolder.

Lines can help separate and group important content, especially when space is limited.
Create a div element below your h1 element, and give it a class attribute set to divider.

The letter-spacing property can be used to adjust the space between each character of text in an element.
Horizontal spacing between equally important elements can increase the readability of your text.

Wrap the text 2/3 cup (55g) in a span element.
Now we can add the horizontal spacing using flex. 

The rem unit stands for root em, and is relative to the font size of the html element.      

The :not pseudo-selector can be used to select all elements that do not match the given CSS rule.

div:not(#example) {
  color: red;
}

The above selects all div elements without an id of example.
The advantage to creating these dividers is that you can apply specific classes to style them individually.