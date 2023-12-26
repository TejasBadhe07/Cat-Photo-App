# Registration Form

You can use HTML forms to collect information from people who visit your webpage.
In this project, you'll learn HTML forms by building a signup page. You'll learn how to control what types of data people can type into your form, and some new CSS tools for styling your page.

The vh unit stands for viewport height, and is relative to 1% of the height of the viewport.
The method attribute specifies how to send form-data to the URL specified in the action attribute. The form-data can be sent via a GET request as URL parameters (with method="get") or via a POST request as data in the request body (with method="post").

The rem unit stands for root em, and is relative to the font size of the html element.

As label elements are inline by default, they are all displayed side by side on the same line, making their text hard to read. To make them appear on separate lines, add display: block to the label element, and add a margin of 0.5rem 0, to separate them from each other.

Specifying the type attribute of a form element is important for the browser to know what kind of data it should expect. If the type is not specified, the browser will default to text.
The email type only allows emails with a @ and a . in the domain. The password type obscures the input, and warns if the site does not use HTTPS.
The first input element with a type of submit is automatically set to submit its nearest parent form element.

To handle the form submission, after the last fieldset element add an input element with the type attribute set to submit and the value attribute set to Submit.
Certain type attribute values come with built-in form validation. For example, type="email" requires that the value be a valid email address.
Add custom validation to the password input element, by adding a minlength attribute with a value of 8. Doing so prevents inputs of less than 8 characters being submitted.

You only want one radio input to be selectable at a time. However, the form does not know the radio inputs are related.

To relate the radio inputs, give them the same name attribute with a value of account-type. Now, it is not possible to select both radio inputs at the same time.
Currently when someone submit the form, they can submit it without checking the radio inputs. Although you had used required attribute to indicate the the input is required previously, this can't work in this case, because adding required to both inputs, will convey the wrong information to the form users.

To solve this, you can provide context of what is needed by adding a legend element with text Account type (required) before the label elements within the second fieldset. Then add the checked attribute to the Personal input to ensure the form is submitted with the required data in it.
Follow accessibility best practices by linking the input elements and the label elements in the second fieldset.