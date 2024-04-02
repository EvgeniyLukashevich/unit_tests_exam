## ОТЧЕТЫ PYLINT
### Модуль с классом ListComparator
```shell
(venv) PS E:\00_Education\0_GeekBrains\705_unit_test\unit_test> pylint list_utils\list_comparator.py
************* Module list_utils.list_comparator
list_utils\list_comparator.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------------------------------------
Your code has been rated at 9.50/10 (previous run: 9.50/10, +0.00)

```
### Модуль с тестами для ListComparator
```shell
(venv) PS E:\00_Education\0_GeekBrains\705_unit_test\unit_test> pylint tests\list_comparator_test.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


```
---
## ОТЧЕТ О ПОКРЫТИИ ТЕСТАМИ (pytest-cov)
Сгенерировать отчет о покрытии тестами можно с помощью команды:
```shell
pytest --cov=list_utils --cov-report=html:coverage_report.html
```
### РЕЗУЛЬТАТ:  
![image](https://github.com/EvgeniyLukashevich/unit_tests_exam/assets/108574612/f4d989d5-50af-43fa-a88b-ff69cd21f6ea)



---

## РЕЗУЛЬТАТ СЕССИИ PYTEST
```shell
(venv) PS E:\00_Education\0_GeekBrains\705_unit_test\unit_test> pytest
================================ test session starts ============================
platform win32 -- Python 3.11.1, pytest-8.1.1, pluggy-1.4.0
rootdir: E:\00_Education\0_GeekBrains\705_unit_test\unit_test
plugins: cov-5.0.0
collected 8 items

tests\list_comparator_test.py ........                                     [100%]

================================= 8 passed in 0.03s =============================

```
