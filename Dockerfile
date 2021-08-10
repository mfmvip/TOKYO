FROM MFMVIP/TOKYO:latest

# نسخ رابط السورس 
RUN git clone https://github.com/MFMVIP/TOKYO.git /root/userbot
# اخـراج العـمل 
WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r resources/setup/requirements.txt

ENV PATH="/home/userbot/resources/setup/bin:$PATH"

CMD ["python3","-m","userbot"]
