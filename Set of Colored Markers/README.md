# CSS Colors by Building a set of Colored Markers

Selecting the correct colors for your webpage can greatly improve the aesthetic appeal to your readers.
Remember that the title element gives search engines extra information about the page. It also displays the content of that title element in two more ways:

in the title bar when the page is open
in the browser tab for the page when you hover on it. Even if that tab is not active, once you hover on the tab, the title text is displayed.
To tell browsers how to encode characters on your page, set the charset to utf-8. utf-8 is a universal character set that includes almost every character from all human languages.

While you have three separate marker div elements, they look like one big rectangle. You should add some space between them to make it easier to see each element.

When the shorthand margin property has two values, it sets margin-top and margin-bottom to the first value, and margin-left and margin-right to the second value.
To give the markers different colors, you will need to add a unique class to each one. Multiple classes can be added to an element by listing them in the class attribute and separating them with a space. For example, the following adds both the animal and dog classes to a div element.

<div class="animal dog">
If you add multiple classes to an HTML element, the styles of the first classes you list may be overridden by later classes.

There are two main color models: the additive RGB (red, green, blue) model used in electronic devices, and the subtractive CMYK (cyan, magenta, yellow, black) model used in print.

In this project, you'll work with the RGB model. This means that colors begin as black, and change as different levels of red, green, and blue are introduced. An easy way to see this is with the CSS rgb function.

A function is a piece of code that can take an input and perform a specific action. The CSS rgb function accepts values, or arguments, for red, green, and blue, and produces a color:

rgb(red, green, blue);
Each red, green, and blue value is a number from 0 to 255. 0 means that there's 0% of that color, and is black. 255 means that there's 100% of that color.

In the additive RGB color model, primary colors are colors that, when combined, create pure white. But for this to happen, each color needs to be at its highest intensity.

Secondary colors are the colors you get when you combine primary colors. You might have noticed some secondary colors in the last step as you changed the red, green, and blue values.

Now that you're familiar with secondary colors, you'll learn how to create tertiary colors. Tertiary colors are created by combining a primary with a nearby secondary color.