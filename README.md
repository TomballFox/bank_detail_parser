# tinkoff_detail_parser
Выписка по расчетному счету Тинькофф парсер

Конвертирует выписку формата pdf в формат xlsx

Структура исходной таблицы:
№ | Дата проведения | Номер докумета | БИК | Счет | Наименование Получ/Отправ. | ВО | По дебету | По кредиту | Назначение платежа
d+| dd.dd.dddd      | d+             | d+  | d+   | String\n                   | dd | d,dd      | d,dd       | String\n

