# Rothko-Painting Readme

Welcome to the Rothko-Painting project documentation! This guide will walk you through the CSS and Box Model techniques used to create Rothko-style rectangular art pieces.

![Rothko Painting](![Rothko-Painting-Design.png])

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

## Adding Rothko Effects

To achieve a Rothko-esque effect, use the `filter` property to blur the painting within the `.canvas` element. For example, applying a 3px blur:

```css
.canvas {
  filter: blur(3px);
}
```

## Softening Edges

Address the issue of sharp edges by increasing the area and softening the edges of the .one element. Set its box-shadow to 0 0 3px 3px #efb762:

```css
.one {
  box-shadow: 0 0 3px 3px #efb762;
}
```

## Round Corners

To further refine the appearance, round each corner of the element by 9 pixels using the border-radius property. This property can accept up to four values for rounding specific corners:

```css
.one {
  border-radius: 9px; /* Applies to all corners */
}
```

Adjust the values for specific corners as needed:

```css
.one {
  border-radius: 9px 0 0 9px; /* Top-left and bottom-left corners */
}
```
Experiment with different values and combinations to achieve the desired softness in the painting's edges.


