# Password Generator

یک برنامه‌ی ساده برای تولید انواع رمز عبور با استفاده از زبان Python.

این پروژه با هدف تمرین مفاهیم **برنامه‌نویسی شیءگرا (OOP)**، از جمله کلاس‌ها، وراثت، کلاس انتزاعی و بازنویسی متدها نوشته شده است.

## قابلیت‌ها

این برنامه می‌تواند سه نوع رمز عبور تولید کند:

### 1. Random Password

تولید رمز تصادفی با استفاده از:

* حروف بزرگ و کوچک انگلیسی
* اعداد (اختیاری)
* نمادها (اختیاری)
* طول دلخواه

### 2. Memorable Password

تولید رمز عبور از چند کلمه‌ی تصادفی انگلیسی.

امکانات:

* تعیین تعداد کلمات
* تعیین جداکننده‌ی کلمات
* امکان بزرگ کردن حرف اول کلمات
* امکان استفاده از واژگان دلخواه

### 3. PIN Code

تولید رمز عددی با طول دلخواه.


## ساختار پروژه

هر سه نوع تولیدکننده از کلاس پایه‌ی `PasswordGenerator` ارث‌بری می‌کنند:

```text
PasswordGenerator
├── RandomPasswordGenerator
├── MemorablePasswordGenerator
└── PinCodeGenerator
```

هر کلاس متد `generate()` را پیاده‌سازی می‌کند و متناسب با نوع رمز، یک رمز عبور تولید می‌کند.


## پیش‌نیازها

برای اجرای پروژه به موارد زیر نیاز دارید:

* Python 3.7 یا بالاتر
* NLTK (Natural Language Toolkit)


## نصب

ابتدا پروژه را دریافت کنید و وارد پوشه‌ی آن شوید.

سپس NLTK را نصب کنید:

```bash
pip install -r requirements.txt
```

## اجرا

برای اجرای برنامه، فایل اصلی پروژه را با Python اجرا کنید:

```bash
python main.py
```


در اولین اجرا، برنامه مجموعه‌ی واژگان مورد نیاز NLTK را دانلود می‌کند:

```python
nltk.download("words")
```

بنابراین برای تولید `Memorable Password`، اتصال اینترنت در اولین اجرا مورد نیاز است.

پس از اجرا، برنامه نمونه‌هایی از هر سه نوع رمز عبور را تولید و نمایش می‌دهد.

برای مثال:

```text
58321
gT7!xP@2
House-Window-River-Mountain
```

مقادیر تولیدشده در هر اجرا تصادفی هستند و ممکن است متفاوت باشند.

## نمونه استفاده

### PIN Code

```python
pin_gen = PinCodeGenerator(5)
print(pin_gen.generate())
```

خروجی نمونه:

```text
58321
```

### Random Password

```python
random_gen = RandomPasswordGenerator(numbers=True, symbols=True)
print(random_gen.generate())
```

خروجی نمونه:

```text
a7@Kp!2x
```

### Memorable Password

```python
mem_gen = MemorablePasswordGenerator(capitalize=True)
print(mem_gen.generate())
```

خروجی نمونه:

```text
House-River-Window-Tree
```

## هدف پروژه

هدف اصلی این پروژه تمرین مفاهیم برنامه‌نویسی شیءگرا و طراحی کلاس‌ها در Python است.

اگرچه برای چنین پروژه‌ی کوچکی می‌توان از توابع ساده نیز استفاده کرد، استفاده از OOP در این پروژه باعث شده ساختار برنامه قابل توسعه‌تر باشد و اضافه کردن روش‌های جدید برای تولید رمز عبور آسان‌تر شود.
