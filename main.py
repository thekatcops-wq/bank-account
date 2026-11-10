class BankAccount:
def init(self, owner, balance=0.0):
self.owner = owner
self.balance = balance
def deposit(self, amount):
    """Метод для поповнення рахунку"""
    if amount > 0:
        self.balance += amount
        print(f"[+] Поповнення на {amount} ")
    else:
        print("[-] Помилка: сума поповнення має бути більшою за нуль.")

def withdraw(self, amount):
    """Метод для зняття грошей"""
    if 0 < amount <= self.balance:
        self.balance -= amount
        print(f"[-] Знято {amount} ")
    else:
        print("[-] Помилка: недостатньо коштів або невірна сума.")

def check_balance(self):
    """Перевірка балансу"""
    print(f"Баланс рахунку {self.owner}: {self.balance}$")

def transfer(self, target_account, amount):
    """Метод для переказу грошей на інший рахунок"""
    if 0 < amount <= self.balance:
        self.balance -= amount
        target_account.balance += amount
        print(f"[->] Переказ {amount}$ для {target_account.owner}. Ваш баланс: {self.balance}$")
    else:
        print("[-] Помилка: недостатньо коштів для переказу.")
Перевірка роботи (цей блок виконається, якщо запустити файл)
if name == "main":
print("--- Створення рахунку ---")
my_account = BankAccount("Ivan", 100.0)
my_account.check_balance()
print("\n--- Транзакції ---")
my_account.deposit(50)
my_account.withdraw(30)
my_account.withdraw(200) # Спроба зняти більше, ніж є