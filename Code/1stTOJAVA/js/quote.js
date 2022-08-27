const quotes = [
    {
        quote: "Đừng so sánh bản thân với người khác. Làm như vậy là bạn đang tự xúc phạm mình đấy ", 
        author: "Bill Gate",
    },
    {
        quote: "Trong một thế giới đang thay đổi rất nhanh chóng, lộ trình duy nhất đưa bạn đến thất bại là không dám mạo hiểm",
        
        author: "Mark Zurkerberg",
    },
    {
        quote: "Thiên tài 1% là cảm hứng và 99% là mồ hôi”",
        author: "Thomas Edison",
    },
    {
        quote: "Nếu bạn không chịu bắt tay vào làm thì chẳng có gì điều gì là khả thi cả",
        author: "Jack Ma",
    },
    {
        quote: "Hãy quay về phía mặt trời và bạn sẽ không thấy bóng tối",
        author: "Hellen Keller",
    },
    {
        quote: "Nếu cho tôi 6 tiếng để đốn hạ 1 cái cây, tôi sẽ dành 4 tiếng đầu tiên để mài rìu",
        author: "Abraha Lincoln",
    },
    {
        quote: "Kẻ nào chưa từng mắc phải lỗi lầm cũng là kẻ chưa bao giờ thử làm việc gì cả",
        author: "Albert Einstein",
    },
    {
        quote: "Cách để bắt đầu đó là cách ngừng nói suông và bắt tay vào công việc",
        author: "Walt Disney",
    },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const TodayQuotes = (quotes[Math.floor(Math.random() * quotes.length)]);

quote.innerText = TodayQuotes.quote;
author.innerText = TodayQuotes.author;