# Urban Routes App Automation Project

### 🎥 Demo Video
<a href="https://drive.google.com/file/d/1dz41bkKlgTeJ7AzlENk1V2D265IlzkLK/view?usp=sharing">Urban Routes Automation</a>

Bootcamp project dedicated to automating end-to-end tests based on the checklist detailed below for the **Urban Routes App**—a ride-hailing application for requesting taxis and passenger transport (similar to Uber).  
The project automates a customized ride request from point A to point B, covering user details such as phone number verification, payment method addition, tariff selection, and specific order requirements.

Key Achievements:
<ul>
  <li><strong>9 test cases created and automated</strong> according to the checklist below.</li>
  <li><strong>100% test coverage achieved.</strong></li>
  <li><strong>Execution time:</strong> Approximately 1 minute.</li>
  <li><strong>Main risk identified:</strong> Missing requirements to define additional positive, negative, and exploratory test scenarios.</li>
</ul>

Project Structure:
<ul>
  <li>
    <strong>Data.py:</strong> Contains test data used across the suite, primarily for populating form inputs and validating UI element text.
  </li>
  <li>
    <strong>Pages.py:</strong> Contains the Page Object Model (POM) locators and interaction methods.
  </li>
  <li>
    <strong>utilities.py:</strong> Features a helper script designed to retrieve the SMS confirmation code for the "Add phone number" flow.
  </li>
  <li>
    <strong>main.py:</strong> Contains the entire test suite execution logic.
  </li>
</ul>

Here is the full test case matrix:

### 📋 Test Case Matrix - Urban Routes

| # | Name | Preconditions | Steps | Expected Result |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Set up the address. | Initialize server | 1. Enter 'East 2nd Street, 601' in "From" field.<br>2. Enter '1300 1st St' in "To" field.<br>3. Validate text in "From" field.<br>4. Validate text in "To" field. | 3. The field text must match the input.<br>4. The field text must match the input. |
| **2** | Select the Comfort tariff. | Initialize server<br>Set up address. | 1. Click "Order a taxi" button.<br>2. Select "Comfort" tariff.<br>3. Validate selection. | 3. The selection state must return "True". |
| **3** | Fill in the phone number. | Initialize server<br>Set up address.<br>Select "Comfort" tariff | 1. Click "Phone number" field.<br>2. Enter '+1 123 123 12 12'.<br>3. Validate the entered phone number.<br>4. Click "Next".<br>5. Enter confirmation code provided by server.<br>6. Validate the entered code.<br>7. Click "Confirm". | 3. The field text must match the input.<br>6. The field text must match the input. |
| **4** | Add a credit card. | Initialize server<br>Set up address.<br>Select "Comfort" tariff | 1. Click "Payment method".<br>2. Click "Add card".<br>3. Enter '1234 5678 9100' in card number field.<br>4. Enter '111' in CVV code field.<br>5. Click outside the input fields.<br>6. Validate text in "Card number" field.<br>7. Validate text in "Code" field.<br>8. Click "Add".<br>9. Click "Close". | 6. The field text must match the input.<br>7. The field text must match the input. |
| **5** | Write a message for the driver. | Initialize server<br>Set up address.<br>Select "Comfort" tariff | 1. Enter 'Show me the way to the museum' in "Message for driver" field.<br>2. Validate text in field. | 2. The field text must match the input. |
| **6** | Order a blanket and tissues. | Initialize server<br>Set up address.<br>Select "Comfort" tariff | 1. Click "Order requirements".<br>2. Toggle "Blanket and tissues".<br>3. Validate switch state. | 3. The switch state must return "True". |
| **7** | Order 2 ice creams. | Initialize server<br>Set up address.<br>Select "Comfort" tariff | 1. Click "+" button on Ice Cream twice.<br>2. Validate counter value. | 2. Counter value must equal "2". |
| **8** | Display taxi search modal. | Initialize server<br>Set up address.<br>Select "Comfort" tariff.<br>Fill in all required fields. | 1. Validate "Order a taxi" label on main action button.<br>2. Click button.<br>3. Validate popup appearance. | 1. Button label must update correctly after filling required fields.<br>3. Popup displaying "Car search..." must appear. |
| **9** | Wait for driver information. | Initialize server<br>Set up address.<br>Select "Comfort" tariff.<br>Fill in all required fields.<br>Order a taxi. | 1. Wait for car search countdown/timer to finish.<br>2. Validate driver details display. | 2. Driver details modal elements must be visible once the timer completes. |

### 🛠️ Prerequisites & Setup

1. **Environment Setup:**  
   Ensure your Python interpreter is configured in PyCharm with `pytest` and `selenium` installed. Recommended dependency versions:
   * **PyTest:** `7.4.4` or higher
   * **Selenium:** `4.11.2` or higher

2. **Server Configuration:**  
   Update the temporary server URL in `data.py` under the `urban_routes_url` variable prior to execution.

### 🚀 How to Run

1. Open the project in **PyCharm 2026.1**.
2. Navigate to `main.py`.
3. Click the **green play button** next to `class TestUrbanRoutes` to run all test cases sequentially.
4. *Note: If running individual test methods, ensure pre-conditions listed in the test matrix are met.*

*Target application URL used during development:*  
`https://cnt-43fafe03-ef9a-41ae-ad3f-851fc792d8c8.containerhub.tripleten-services.com/?lng=es`

---
*Built with **PyTest** and **Selenium WebDriver** using **Object-Oriented Programming (OOP)**, **Page Object Model (POM)** pattern, and DOM manipulation. Version control managed via **Git Bash** and **GitHub**.*
