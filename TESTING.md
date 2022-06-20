# TESTING

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[What You Need :arrow_right:](https://connect-with.herokuapp.com/)**.

## Table of Content

* [Code Validation](#Code-Validation)
  * [W3C](#W3C)
  * [JSHint](#JSHint)
  * [PEP8](#PEP8)
* [Lighthouse](#Lighthouse)
* [Cross Browsers Testing](#Cross-Browsers-Testing)
* [Manual Testing](#Manual-Testing)
  * [Functionality Testing](#Functionality-Testing)
    * [Home](#Home)
    * [Contact us](#Contact-us)
* [User Stories Testing](#User-Stories-Testing)

## Code Validation

All code validation has been done using text input. The code was copied from the source code in the browser. This allows to check HTML without getting error because of Jinja templating language.

### W3C

W3C Markup Validation Service and W3C CSS Validation Service have been used to check all the pages of the website for semantic and syntax errors.
The results show no errors and the code is valid.

* [W3C Markup Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

### JSHint

[JSHint](https://jshint.com/) was used to validate the JavaScript code for semantic and syntax errors. No warnings or error were found.  
The results are positive, and the code is valid.

### PEP8

[PEP8 online](http://pep8online.com/) was used to validate the Python code for semantic and syntax errors.  
The results are positive, and the code is valid.  

* 3 warnings were found:
Two of those warnings are comming from signals beeing imported in apps.py of the checkout and products apps. They are designed to be used that way from my best knowledge and therefore were left with the warning.  
The third warning is for 3 line too long from the Django boilerplate in settings.py.

When running flake8 in the terminal the only other warnings are coming for auto-generated files from django (migrations).

## Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) is a tool provided by Google Chrome DevTools and allows to identify the site performance, accessibility and user experience on Mobile and Desktop.  
All the pages from the website have been tested with Lighthouse.

Score given by the lighthouse are very good for the exception of performance issue on smartphone and some contrast issue that are negligeable.

![lightouse score for home page](documentation/features/lighthouse-home.png)
![lightouse score for shopping bag page](documentation/features/lighthouse-bag.png)
![lightouse score for messages page](documentation/features/lighthouse-messages.png)
![lightouse score for order history page](documentation/features/lighthouse-orders.png)
![lightouse score for products page](documentation/features/lighthouse-products.png)
![lightouse score for store management page](documentation/features/lighthouse-store.png)
![lightouse score for wishlist page](documentation/features/lighthouse-wishlist.png)

[**:back:** *Table of Content*](#Table-of-Content)

## Manual Testing

* Manual testing was executed on several browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari and Opera) and shows good functionality across them all.
* The responsiveness of the website for different viewport sizes was tested by dragging the window up, down, left and right.  
* The following tests have been executed several times at different viewport breakpoints and on different devices.  
* Friends, fellow Code Institute students and family members tested the website on different devices.

### Functionality Testing

#### General features

* Buttons change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Link change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Forms validation
  * inputs/ content :heavy_check_mark:
  * on submit :heavy_check_mark:
* Modal Triggers :heavy_check_mark:
