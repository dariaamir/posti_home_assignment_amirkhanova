This is a test task for a job application.

**Task scope:**

Go to https://www.posti.fi/en and add stamps of your choosing to the cart. Validate that the total and delivery fees are calculated correctly, also after updating the cart with an additional product.

Upon checkout (without needing to buy, of course), check that the validation of a Finnish postal code works as expected (5 digits). 

**Project structure:**

Test is located in the  `/tests` folder : there is test case description in the  .txt file and robot framework script in the .robot file.

`/resources` folder contains additional files, such as page objects for each page (.py and .robot files), `setup.robot` file with test setup configuration. And `utils.py` with additional python scripts.

Reports will be generated after the test run in the `/reports` folder. If test fails, reports will also include screenshot of the failure.


**Technologies used:**

- Robot Framework
- Python
- Selenium

**To run the test:**

`robot -d reports tests/add_stamps_into_cart_and_checkout.robot
`