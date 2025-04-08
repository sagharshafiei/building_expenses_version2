# building_expenses
A program for management and payment of monthly apartment charges and bills, such as: "water bills, gas charges, cleaning costs, ..." with MVC Framework

This project has 2 key roles with 2 separate sections for each role, And each role is automatically detected by the program via the login action(The program checks the entered username/password with Database):
1. **Admin**: The Admin user can add and remove a unit, or edit each units information(such as unit no., residents count in each unit, ...)
it can also do the same with monthly-building expenses; although its necessary to mention that the Admin role enters the TOTAL-monthly-charges for the whole building for each item, meaning that the bills are automatically calculated and shown for each unit based on the resident count of that unit.
for example:
Esfand's Water Bill(for the whole apartment): 1,000,000 Tomans  --->  A Total Number Of 10 People Live In That Apartment  --->  Esfand's Water Bill(per person) = 1,000,000 / 10 = 100,000 Tomans  ---> A Unit (e.g. unit 2) Has 3 Residents  --->  The Water Bill That Unit Has To Pay Equals To: 3 x 100,000 = 300,000 Tomans

2. **User**: Each User's window can be opened after the right username/password of that Unit has been entered. in User's window, a table of each month's charges is shown and the user can pay the latest charges which is done by pressing the "Pay" Button, which takes the user to the Payment Window.
