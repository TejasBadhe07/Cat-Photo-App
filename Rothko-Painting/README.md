# Rothko-Painting Readme

Welcome to the Rothko-Painting project documentation! This guide will walk you through the CSS and Box Model techniques used to create Rothko-style rectangular art pieces.

## Box Model Basics

In the CSS box model, every HTML element is treated as a box with distinct areas:

1. **Content:**
   - The actual content of the box, such as text, images, or other elements.

2. **Padding:**
   - The space surrounding the content, similar to the padding in a shipped item's box.

3. **Border:**
   - Represents the outer boundary of the box, analogous to the cardboard box of a shipped item.

4. **Margin:**
   - The area outside the box, influencing the space between other boxes or elements.

Even a seemingly empty `<div>` is treated as a box with content. To demonstrate, create a CSS rule for the `.canvas` class, setting its width to 500 pixels:

```css
.canvas {
  width: 500px;
}
```
