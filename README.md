# Midterm
## კორელაციის მოძებნა
### ნაბიჯი 1
ამოიწერა ყველა წერტილის x და y კოორდინატები:

x = [-9.5, -6.2, -5, -1.5, 1, 3, 5, 7]

y = [1, 2, -1, 0.1, -2, 0, -3, -2]

### ნაბიჯი 2
გამოითვალა საშუალო მნიშვნელობები x და y მონაცემებისთვის:

x საშ = -0.775, y საშ = -0.6125

### ნაბიჯი 3
იმის გამო, რომ მონაცემთა ცალ-ცალკე დამუშავებას ძალიან დიდი დრო დასჭირდება, მიზანშეწონილია პითონის ბიბლიოთეკების გამოყენება შემდეგი ნაბიჯების შესასრულებლად:

        import numpy as np
        x = np.array([-9.5, -6.2, -5, -1.5, 1, 3, 5, 7])
        y = np.array([1, 2, -1, 0.1, -2, 0, -3, -2])
        x_mean = np.mean(x)
        y_mean = np.mean(y)

სხვაობების გამოთვლა:

        x_diff = x - x_mean
        y_diff = y - y_mean

### ნაბიჯი 4
მრიცხველის და მნიშვნელის ნამრავლების გამოთვლა:

        xy_diff_product = x_diff * y_diff
        x_diff_sq = x_diff ** 2
        y_diff_sq = y_diff ** 2

### ნაბიჯი 5
ნამრავლების შეჯამება მრიცხველში:

        numerator = np.sum(xy_diff_product)

### ნაბიჯი 6
ნამრავლების შეჯამება, გამრავლება და ფესვის ამოყვანა მნიშვნელში:

        denominator = np.sqrt(np.sum(x_diff_sq)) * np.sqrt(np.sum(y_diff_sq))

### ნაბიჯი 7
მიღებული მნიშვნელობების ერთმანეთზე გაყოფა:

        r = numerator / denominator

### შედეგი
პირსონის კორელაციის კოეფიციენტი -0.7558910476323901-ის ტოლია, რაც ორ ცვლადს შორის (x და y) საკმაოდ ძლიერ უკუდამოკიდებულებას აჩვენებს. უკეთესი გაგებისთვის ავაგოთ გაბნევის გრაფიკი:

        import matplotlib.pyplot as plt
        plt.figure(figsize=(7, 5))
        plt.scatter(x, y, color='blue', edgecolor='black')
        plt.title('x და y კოორდინატების გაბნევის გრაფიკი')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.tight_layout()

![გრაფიკის მისამართი] https://github.com/Nodar-Melkonyan/midterm/blob/main/Scatter%20plot.png

გრაფიკზე ჩანს, რომ y-მნიშვნელობების კლებისას, x-მნიშვნელობები იზრდება, რაც ადასტურებს მიღებულ კოეფიციენტს.




## სპამ ელ-ფოსტის გამოვლენა
### 1. ![მოცემული დავალება შესრულებულია შემდეგ მონაცემთა ნაკრებზე] https://github.com/Nodar-Melkonyan/midterm/blob/main/nodar_melkonyan_1_81429765.csv

### 2. ![ლოგისტიკური რეგრესიის პროგრამა] https://github.com/Nodar-Melkonyan/midterm/blob/main/Logistic_Regression.py

მონაცემების წაიკითხა pandas ბიბლიოთეკის read_csv() ფუნქციის მეშვეობით შესაბამის დირექტორიაში მოთავსებული ფაილიდან:

        df = pd.read_csv("nodar_melkonyan_1_81429765.csv")

შემდეგ, მონაცემები დაიყო ორად: პარამეტრებად, რომლებსაც შეუძლიათ ზეგავლენა ჰქონდეთ სამიზნეზე: არის თუ არა სპამი შესაბამისი წერილი:

        X = df[['words', 'links', 'capital_words', 'spam_word_count']]
        y = df['is_spam']

მონაცემების მომდევნო დაყოფა გასაწვრთნ და სატესტო ნაკრებებად შემდეგი დამუშავებისთვის, სადაც გასაწვრთნი მონაცემების წილი 70% არის:

        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

შესაბამისი მოდელი და გაწვრთნა:

        model = LogisticRegression()
        model.fit(X_train, y_train)

კოეფიციენტების გამოთვლა:

        coefficients = pd.Series(model.coef_[0], index=X.columns)
        print (coefficients)

შედეგები:

words              0.006916
links              0.915510
capital_words      0.517343
spam_word_count    0.786174

ჩანს, რომ სიტყვების რაოდენობას არ აქვს რაიმე არსებითი გავლენა სპამ-წერილების ამოცნობაში. ამავდროულად, თითქმის ბმულების რაოდენობა უმნიშვნელოვანესი ფაქტორია ასეთი წერილების გამოსავლენად. გამოირჩევა, ასევე, სპამ-სიტყვები, თუმცა არა ისეთი "სიძლიერით", როგორც ბმულები. დიდი ასოების შემცველ სიტყვებზე კი ცალსახა პასუხს ვერ გავცემთ: 0.517343 არ იძლევა საკმარის ინფორმაციას ამ პარამეტრის გავლენაზე.
საბოლოო ჯამში, რაც უფრო მეტი ბმული და სპამ-სიტყვა აქვს წერილს, მიტ უფრო დიდი ალბათობით ის იქნება სპამი.

### 3. მონაცემების შემოწმება სატესტო ნაკრებზე

        y_pred = model.predict(X_test)

აღრევის მატრიცის შექმნა. ამისთვის შესაბამის ფუნქციას congusion_matrix გადავცემთ ორ პარამეტრს: რეალურ მონაცემებს სპამ წერილებზე და მოდელი მიერ გადამოწმებულ/ნაწინასწარმეტყველებ შედეგებს სპამ წერილებზე (y_pred): 

        cm = confusion_matrix(y_test, y_pred)

აღრევის მატრიცის შედეგი

        [[378,  17],
       [ 15, 340]]
718 შემთხვევაში (378+340) მოდელმა სწორად განსაზღვრა სპამი და არა სპამ-წერილები, ცოლო 32-ში — შეცდა.
![უკეთესი აღქმისთვის გაეცანით აღრევის მატრიცის გრაფიკულ გამოსახულებას] https://github.com/Nodar-Melkonyan/midterm/blob/main/Confusion_Matrix.png

y-ღერძზე დატანილი მონაცემები ჭდე მნიშვნელობებია, ანუ რაც რეალურად არსებობს. ხოლო აბსცისას მონაცემები უკვე მოდელის მიერ გამოთვლილი/კლასიფიცირებული მნიშვნელობებია. მატრიციდან ჩანს, რომ 378 წერილი რეალურად არ იყო სპამი და მოდელმაც სწორად განსაზღვრა იგი (ზედა ლურჯი უჯრა). 340 წერილი იყო სპამი, რომლებიც მოდელმა, ასევე, სწორად ამოიცნო (ქვედა ლურჯი უჯრა). ქვედა მარცხენა უჯრაში ვხედავთ, რომ 15 წერილი იყო რეალურად სპამი, მაგრამ მოდელი ვერ მიხვდა ამას. დარჩენილ ზედა მარჯვენა უჯრაში ვხედავთ, რომ 17 წერილი არ იყო სპამი, თუმცა აქაც მოდელი წარუმატებელი აღმოჩნდა, — ისინი სპამად დაახარისხა.

მატრიცის შესაქმნელად გამოყენებულ იქნა შემდეგი კოდი:

        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not Spam", "Spam"])
        disp.plot(cmap="Blues")
        plt.title("Confusion Matrix")

### 4. პროგრამა, რომელიც სპამ-წერილებს ამოიცნობს

#### ნაბიჯი 1
ამ ამოცანის შესასრულებლად სიმარტივისთვის ჩემი მოდელი შევინახე პითონ-ობიექტად .pkl-ფორმატის ბინარული ფაილის სახით, რომელიც შემდეგ გამოყენებული იქნება უშუალოდ სპამ-ამომცნობ პროგრამაში.

![ლოგისტიკური რეგრესიის მოდელი] https://github.com/Nodar-Melkonyan/midterm/blob/main/Model.py

![.pkl ფაილი] https://github.com/Nodar-Melkonyan/midterm/blob/main/spam_model.pkl

### ნაბიჯი 2
ამ ამოცანის შესასრულებლად დაწერილი იქნება პროგრამა, რომელიც დათვლის შესაბამის პარამეტრებს: სიტყვების, ბმულების, დიდი ასოებისგან შემდგარი სიტყვებისა და სპამ-სიტყვების რაოდენობას. გამოყენბული იქნება ბიბლიოთეკა re.

        import re

ზოგიერთი ხშირი სპამ სიტყვის ჩამონათვალი:

        SPAM_WORDS = [
            "free", "win", "click", "offer", "winner", "buy", "limited",
            "guarantee", "urgent", "claim", "prize", "cash", "now", "exclusive",
            "risk-free", "trial", "act now", "credit", "cheap", "save", "instant"
        ]

ფუნქციის დაწყება:

        def extract_email_features(text):
        
სიტყვების რაოდენობის დათვლა:

            words = re.findall(r'\b\w+\b', text)
            total_words = len(words)
        
ბმულების რაოდენობის დათვლა:

            links = len(re.findall(r'(http[s]?://|www\.)\S+', text))
        
დიდი ასოებისგან შემდგარი სიტყვების რაოდენობა, გარდა ერთასოებიანებისა:

            capital_words = sum(1 for word in words if word.isupper() and len(word) > 1)
        
სპამ-სიტყვების დათვლა:

            spam_word_count = sum(1 for word in words if word.lower() in SPAM_WORDS)

შედეგი:

            return {
                "words": total_words,
                "links": links,
                "capital_words": capital_words,
                "spam_word_count": spam_word_count
            }

ასე, დავთვლით ჩვენთვის მნიშვნელოვანი პარამეტრების რაოდენობას.

![სიტყვების მთვლელი პროგრამა] https://github.com/Nodar-Melkonyan/midterm/blob/main/Counter.py

### ნაბიჯი 3

პროგრამის დაწერა, რომელშიც ჩავაშენებთ .pkl ფაილს, მივცემთ ზედა პროგრამის მეშვეობით დათვლილ მონაცემებს და მივიღებთ შედეგს:

ვტვირთავთ შესაბამის ბიბლიოთეკებს:

        import pickle
        import numpy as np

ვტვირთავთ .pkl ფაილს:

        with open("spam_model.pkl", "rb") as f:
            model = pickle.load(f)
            
ვქმნით ფუნქციას შესაბამისი პარამეტრებით:

        def check_if_spam(words, links, capital_words, spam_word_count):

პარამეტრებს გადავაკეთებთ 2-განზომილებიან მატრიცად:

        features = np.array([[words, links, capital_words, spam_word_count]])

ვარკვევთ, არის თუ არა წერილი სპამი, და რამდენია ამის ალბათობა:

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

შედეგს ვიღებთ შემდეგი სახით:

        if prediction == 1:
                print(f"🚨 This message is likely SPAM (probability = {probability:.2f})")
        else:
                print(f"✅ This message is NOT spam (probability = {probability:.2f})")

![სპამის შემმოწმებელი პროგრამა] https://github.com/Nodar-Melkonyan/midterm/blob/main/Spam_checker.py

ამ პროგრამების გაერთიანებული მუშაობით მივიღებთ ჩვენთვის საჭირო შედეგს. შემდეგ მაგალითებზე უკეთ ვნახავთ ამ ფუნქციების მუშაობას.

### 5. სპამ-წერილის მაგალითი

WIN BIG NOW! CLICK the link below to claim your FREE iPhone. This is a LIMITED TIME OFFER. Visit http://spamlink.com and enter your information to WIN TODAY!

ეს ტექსტი შეადგინა Chat GPT-მ შესაბამისი ინსტრუქციების მიხედვით (ვგულისხმობ, პარამეტრების გათვალისწინებით: ამ შემთხვევაში ბევრი სპამ სიტყვა, ერთი ბმული 29-ასოიანი ტექსტისთვის და დიდი ასოების გამოყენება ცალკეული სიტყვებისთვის).

#### პირველი ნაბიჯი იქნება ტექსტის მთვლელ ფუნქციაში ჩასმა და პარამეტრების რაოდენობების გარკვევა:

        extract_email_features("WIN BIG NOW! CLICK the link below to claim your FREE iPhone. This is a LIMITED TIME OFFER. Visit http://spamlink.com and enter your information to WIN TODAY!")

შედეგი:

        {'words': 29, 'links': 1, 'capital_words': 10, 'spam_word_count': 8}

#### ამ მონაცემების აღების შემდეგ მათ სპამის შემმოწმებელ პროგრამაში ჩავსვამთ:

        check_if_spam(words=29, links=1, capital_words=10, spam_word_count=8)

შედეგი: This message is likely SPAM (probability = 0.95)

ანუ, პროგრამამ ზემოთ მოცემული ტექსტი 95%-იანი ალბათობით სპამად მიიჩნია.

### 6. გავიმეოროთ იგივე ქმედებები ნორმალურ ტექსტთან:

Hi Emily,

I hope you're doing well. I just wanted to follow up on our meeting next week regarding the product roadmap. I've attached the updated presentation, and let me know if there's anything you’d like to discuss in more detail.

Also, please confirm the time — I have 10:30 AM on Wednesday penciled in. Looking forward to it!

Best regards,  
Alex

ტექსტი, ასევე, დაგენერირებულია Chat GPT-ის მიერ.

        extract_email_features ("Hi Emily, I hope you're doing well. I just wanted to follow up on our meeting next week regarding the product roadmap. I've attached the updated presentation, and let me know if there's anything you’d like to discuss in more detail. Also, please confirm the time — I have 10:30 AM on Wednesday penciled in. Looking forward to it! Best regards, Alex")

აქ უკვე აღარ ჩანს სპამ-სიტყვები, ბმულები და დიდი ასოები ცალკეულ სიტყვებში.

შედეგი:

        {'words': 66, 'links': 0, 'capital_words': 1, 'spam_word_count': 0}


მიღებული მონაცემების შეყვანა სპამის შემმოწმებელ პროგრამაში:

        check_if_spam(words=66, links=0, capital_words=1, spam_word_count=0)

შედეგი:

        This message is NOT spam (probability = 0.00)

ეს წერილი აღარ არის სპამი. სპამის ალბათობა 0-ის ტოლია.
