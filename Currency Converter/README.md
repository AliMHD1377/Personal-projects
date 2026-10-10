# به نام خدا

# 💵 مبدل ارز (Currency Converter)

یک مبدل ارز ساده و سریع که با **Streamlit** ساخته شده و نرخ‌های لحظه‌ای ارزها رو از **ExchangeRate-API** می‌گیره.

## ✨ امکانات

- تبدیل آنی بین بیش از ۱۶۰ ارز مختلف
- دریافت نرخ لحظه‌ای از API معتبر
- بدون نیاز به دکمه — به‌محض تغییر مقدار یا ارز، نتیجه به‌روز می‌شه
- نمایش زمان آخرین به‌روزرسانی نرخ (به‌صورت خوانا با `humanize`)
- کش کردن نرخ‌ها به مدت ۵ دقیقه برای کاهش درخواست‌های تکراری

## 🛠️ نصب و اجرا

### ۱. کلون کردن پروژه

```bash
git clone https://github.com/AliMHD1377/Personal-projects.git
cd Personal-projects/Currency-Converter
```

### ۲. ساخت محیط مجازی (اختیاری ولی توصیه‌شده)

```bash
python -m venv venv
source venv/bin/activate        # لینوکس / مک
venv\Scripts\activate           # ویندوز
```

### ۳. نصب پکیج‌های مورد نیاز

```bash
pip install -r requirements.txt
```

### ۴. اجرای برنامه

```bash
cd src
streamlit run app.py
```

بعد از اجرا، مرورگر به‌صورت خودکار باز می‌شه و آدرس معمولاً `http://localhost:8501` هست.

## 📁 ساختار پروژه

```
currency-converter/
├── src/
│   ├── app.py              # رابط کاربری Streamlit
│   └── main.py             # منطق دریافت نرخ و تبدیل ارز
├── requirements.txt
└── README.md
```

## 🧠 نحوه کار

1. کاربر مقدار و ارز مبدأ و مقصد رو انتخاب می‌کنه.
2. تابع `get_exchange_rate` نرخ رو از API می‌گیره (با کش ۵ دقیقه‌ای).
3. تابع `convert_currency` مقدار رو در نرخ ضرب می‌کنه.
4. نتیجه همراه با زمان آخرین به‌روزرسانی نمایش داده می‌شه.

## 📦 پکیج‌های استفاده‌شده

| پکیج | کاربرد |
|------|--------|
| `streamlit` | ساخت رابط کاربری وب |
| `requests` | ارسال درخواست به API |
| `cachetools` | کش کردن نرخ‌ها |
| `humanize` | نمایش خوانای زمان |
| `currencies` | لیست کدهای ارز |
