# Basic CSS: Cafe Menu Design

This project focuses on using CSS to create a stylish menu page for a cafe website. CSS (Cascading Style Sheets) is essential for controlling the presentation and layout of HTML elements.

## CSS Basics

- **Role of CSS:** Instructs the browser on how to display webpage elements, defining colors, fonts, and sizes.

- **Page Title:** Provides extra information for search engines and page display.

- **Div Element:** Used for design layout purposes.

- **Styling with Classes:** Apply styling using classes by adding a class attribute to the div element.

- **Article Elements:** Contain multiple items with related information for structured content.

- **Divider Usage:** Employ the hr element to create dividers between content sections.

## Applying Styles

## Applying Styles

Use the following syntax to apply styles:

```css
element {
  property: value;
}


For multiple elements, create a list of selectors:

css
Copy code
selector1, selector2 {
  property: value;
}
CSS Comments
Use this syntax for comments:

css
Copy code
/* Comment Here */
Class Selectors
Define class selectors with a dot preceding the name:

css
Copy code
.class-name {
  styles
}
External Style Sheets
For better organization, place styles in a separate file and link to it.

Responsive Design
Ensure consistent styling on both desktop and mobile with a meta element.

Centering Elements
To center an element horizontally, set margin-left and margin-right properties to auto.

You change properties of a link when the link has actually been visited by using a pseudo-selector that looks like a:visited { propertyName: propertyValue; }.

You change properties of a link when the mouse hovers over them by using a pseudo-selector that looks like a:hover { propertyName: propertyValue; }.

You change properties of a link when the link is actually being clicked by using a pseudo-selector that looks like a:active { propertyName: propertyValue; }.