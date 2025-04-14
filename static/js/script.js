/*==================== toggle icon navbar ====================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

/*==================== scroll sections active link ====================*/
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        }
    });

    let header = document.querySelector('header');
    header.classList.toggle('sticky', window.scrollY > 100);

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
};

/*==================== scroll reveal ====================*/
ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
});

ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', { origin: 'bottom' });
ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });
ScrollReveal().reveal('.home-content p, .about-content', { origin: 'right' });

/*==================== typed js ====================*/
const typed = new Typed('.multiple-text', {
    strings: ['Professional hairdresser', 'Colorist', 'Stylist'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});

/*==================== Comments API ====================*/
const API_URL = "/api/comments"; // Проверьте корректность API_URL
let selectedRating = 0;

// Load comments from server
async function loadComments() {
    try {
        const response = await fetch(API_URL, {
            method: 'GET',
            mode: 'cors' // Добавляем режим cors
        });
        console.log('Fetching comments...'); // Отладочное сообщение
        if (!response.ok) throw new Error(`Ошибка загрузки комментариев: ${response.statusText}`);

        const comments = await response.json();
        const commentList = document.getElementById('comments-list');
        commentList.innerHTML = '<h3>Отзывы:</h3>';

        comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.classList.add('comment');
            commentElement.innerHTML = `
                <div class="rating">${'★'.repeat(comment.rating)}${'☆'.repeat(5 - comment.rating)}</div>
                <p>${comment.comment}</p>
            `;
            commentList.appendChild(commentElement);
        });
    } catch (error) {
        console.error('Ошибка подключения:', error);
        alert('Не удалось загрузить комментарии. Попробуйте позже.');
    }
}

// Submit comment to server
document.getElementById('comment-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const commentText = document.getElementById('comment-text').value;
    if (!selectedRating) return alert('Пожалуйста, выберите оценку!');
    if (!commentText.trim()) return alert('Пожалуйста, напишите комментарий!');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rating: selectedRating, comment: commentText }),
        });
        console.log('Response status:', response.status); // Отладочное сообщение
        console.log('Response body:', await response.text()); // Отладочное сообщение

        if (!response.ok) throw new Error('Ошибка при добавлении комментария.');

        await loadComments();
        document.getElementById('comment-form').reset();
        document.querySelectorAll('.stars span').forEach(s => s.classList.remove('selected'));
        selectedRating = 0;
    } catch (error) {
        console.error('Ошибка подключения:', error);
        alert('Не удалось отправить комментарий. Попробуйте позже.');
    }
});

// Select star rating
document.querySelectorAll('.stars span').forEach(star => {
    star.addEventListener('click', () => {
        selectedRating = parseInt(star.getAttribute('data-star'));
        document.getElementById('rating').value = selectedRating;

        document.querySelectorAll('.stars span').forEach(s => {
            const val = parseInt(s.getAttribute('data-star'));
            if (val <= selectedRating) {
                s.classList.add('selected');
            } else {
                s.classList.remove('selected');
            }
        });
    });
});

// Hover-подсветка
document.querySelectorAll('.stars span').forEach(star => {
    star.addEventListener('mouseover', () => {
        const hoverValue = parseInt(star.getAttribute('data-star'));
        document.querySelectorAll('.stars span').forEach(s => {
            const val = parseInt(s.getAttribute('data-star'));
            s.classList.toggle('selected', val <= hoverValue);
        });
    });

    star.addEventListener('mouseout', () => {
        document.querySelectorAll('.stars span').forEach(s => {
            const val = parseInt(s.getAttribute('data-star'));
            s.classList.toggle('selected', val <= selectedRating);
        });
    });
});


// Load comments on page load
document.addEventListener('DOMContentLoaded', loadComments);


/*==================== Snowflakes ====================*/
/*
function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    snowflake.style.left = Math.random() * 100 + 'vw';
    snowflake.style.animationDuration = Math.random() * 10 + 10 + 's';
    snowflake.style.opacity = Math.random();
    snowflake.style.fontSize = Math.random() * 12 + 8 + 'px';
    snowflake.textContent = '❄';

    document.getElementById('snow-container').appendChild(snowflake);

    setTimeout(() => snowflake.remove(), parseFloat(snowflake.style.animationDuration) * 1000);
}
// Определяем интервал в зависимости от ширины экрана
const interval = window.innerWidth <= 768 ? 20000 : 500; // 500ms для телефонов, 50ms для ПК

setInterval(createSnowflake, interval);
*/

// Загрузка комментариев при загрузке страницы
document.addEventListener('DOMContentLoaded', loadComments)


// Open and close modals
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "block"; // Открываем модальное окно
    } else {
        console.error(`Модальное окно с id="${modalId}" не найдено.`);
    }
}


function closeModal(modalId) {
    if (!modalId) {
        console.error('Не передан id модального окна.');
        return;
    }

    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none"; // Закрываем модальное окно
    } else {
        console.error(`Модальное окно с id="${modalId}" не найдено.`);
    }
}

// Close modal on background click
document.addEventListener('click', function (event) {
    const modal = document.querySelector('.modal');
    if (modal && event.target === modal) {
        modal.style.display = "none";
    }
});

// Close modal on Escape

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        const modal = document.querySelector('.modal');
        if (modal) {
            modal.style.display = "none";
        }
    }
});



// Хранение переводов
const translations = {
    ru: {
        "haircuts.title": "Стрижки",
        "haircuts.description": "Я выполняю современные стрижки любой сложности, учитывая индивидуальные пожелания клиента.",
        "coloring.title": "Окрашивание",
        "coloring.description": "Использую лучшие материалы и современные техники для создания идеального цвета.",
        "styling.title": "Укладка",
        "styling.description": "Создаю укладки для любого случая: повседневные, вечерние и свадебные.",
        "more": "Подробнее",
    },
    en: {
        "haircuts.title": "Haircuts",
        "haircuts.description": "I perform modern haircuts of any complexity, taking into account the client's individual wishes.",
        "coloring.title": "Coloring",
        "coloring.description": "I use the best materials and modern techniques to create the perfect color.",
        "styling.title": "Styling",
        "styling.description": "I create hairstyles for any occasion: casual, evening, and wedding styles.",
        "more": "Learn More",
    },
    uz: {
        "haircuts.title": "Soch olish",
        "haircuts.description": "Men mijozning shaxsiy istaklarini hisobga olgan holda har qanday murakkablikdagi zamonaviy sochlarni bajara olaman.",
        "coloring.title": "Rang berish",
        "coloring.description": "Men eng yaxshi materiallardan va zamonaviy texnikalardan foydalanib, mukammal rang yarataman.",
        "styling.title": "Soch turmaklash",
        "styling.description": "Har qanday holat uchun: oddiy, kechki va to‘y uslublari uchun soch turmaklayman.",
        "more": "Batafsil",
    }
};

let currentLanguage = "en"; // Язык по умолчанию


function initStars() {
    document.querySelectorAll('.stars span').forEach(star => {
        star.addEventListener('click', () => {
            selectedRating = star.getAttribute('data-star');

            // Обновляем значение скрытого поля
            document.getElementById('rating').value = selectedRating;

            // Обновляем визуальное состояние звезд
            document.querySelectorAll('.stars span').forEach(s => s.classList.remove('selected'));
            star.classList.add('selected');
        });
    });
}

// Обновление текста на странице
function updateLanguage(lang) {
    currentLanguage = lang;

    // Перебираем элементы с атрибутом data-translate
    document.querySelectorAll("[data-translate]").forEach(el => {
        const key = el.getAttribute("data-translate");
        const translation = translations[currentLanguage][key];
        if (translation) {
            el.innerText = translation;
        }
    });
}

    // Обновляем активный язык
    document.querySelectorAll('.lang-switch').forEach(link => {
        link.classList.toggle('active', link.getAttribute('data-lang') === currentLanguage);
    });

    // Инициализируем обработчики для звёздочек заново
    initStars();


// Обработчик переключения языка
document.querySelectorAll('.lang-switch').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const lang = link.getAttribute('data-lang');
        updateLanguage(lang);
    });
});

// Инициализация интерфейса
document.addEventListener('DOMContentLoaded', () => {
    updateLanguage(currentLanguage);
});
