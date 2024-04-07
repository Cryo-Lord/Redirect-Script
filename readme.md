This project uses pandas, and urllib

This script ask for a route of an .csv or .xlsx file in the format:

| URL | Redirected URL | Status |

URL: where the URL is the visited url
Redirected URL: is what url is suppossed to redirect once visited last url; if there is no one, output on Status will change
Status: where the answer is written: "Not redirected", "Redirected", "REDIRECTED" and "REDIRECTED TO UNEXPECTED URL"

The capitalized answers are the expected and good answers, where the script visited the url and when is redirected to the inputed url succesfully.

The answers with all capital letters are the error answers, where the redirection occurs and when the redirected URL was different to the expected one.