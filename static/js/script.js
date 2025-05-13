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

/*==================== typed.js — многоязычный ====================*/

let typed = null;

const typedStrings = {
    ru: ['Парикмахер-стилист', 'Колорист', 'Мастер причесок'],
    en: ['Professional hairdresser', 'Colorist', 'Stylist'],
    uz: ['Soch stilisti', 'Kolorist', 'Soch ustasi']
};

function updateTypedText(lang) {
    if (typed) typed.destroy();

    typed = new Typed('.multiple-text', {
        strings: typedStrings[lang] || typedStrings.en,
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
    });
}


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
        "haircuts.description": "Выполняю современные стрижки любой сложности, учитывая индивидуальные пожелания клиента.",
        "coloring.title": "Окрашивание",
        "coloring.description": "Использую лучшие материалы и современные техники для создания идеального цвета.",
        "styling.title": "Укладка",
        "styling.description": "Создаю прически для любого случая: повседневные, вечерние и для различных мероприятий.",
        "more": "Подробнее",

        // ✅ Строки секции home
        "home.greeting": "Здравствуйте, Меня зовут",
        "home.i_am": "Я",
        "home.services": "Выполняю все виды стрижек, укладок и техники окрашивания любой сложности.",
        "home.approach": "Индивидуальный подход к каждому клиенту.",

        // ✅ Комментарии
        "comments.reviews": "Отзывы:",
        // ✅ добавляем
        "telegram.review": "Оставить отзыв через Telegram"
    },

    en: {
        "haircuts.title": "Haircuts",
        "haircuts.description": "Provide modern haircuts of any complexity, considering the individual preferences of the client.",
        "coloring.title": "Coloring",
        "coloring.description": "Use the best materials and modern techniques to create the perfect color.",
        "styling.title": "Styling",
        "styling.description": "Create hairstyles for any occasion: casual, evening, and for various events.",
        "more": "Learn More",

        // ✅ Строки секции home
        "home.greeting": "Hello, my name is",
        "home.i_am": "I am",
        "home.services": "I perform all types of haircuts, styling, and coloring techniques of any complexity.",
        "home.approach": "An individual approach to every client",

        // ✅ Комментарии
        "comments.reviews": "Reviews:",
        "telegram.review": "Leave a review via Telegram"
    },

    uz: {
        "haircuts.title": "Soch olish",
        "haircuts.description": "Mijozning istaklariga mos har qanday murakkablikdagi zamonaviy soch turmaklarini bajaraman.",
        "coloring.title": "Rang berish",
        "coloring.description": "Ideal rangga erishish uchun eng yaxshi materiallar va zamonaviy texnikalardan foydalanaman.",
        "styling.title": "Soch turmaklash",
        "styling.description": "Har qanday holat uchun soch turmaklari yarataman — oddiy, kechki va bayramona tadbirlar uchun.",
        "more": "Batafsil",

        // ✅ Строки секции home
        "home.greeting": "Salom, mening ismim",
        "home.i_am": "Men",
        "home.services": "Har qanday murakkablikdagi soch olish, turmaklash va bo‘yash texnikalarini bajaraman.",
        "home.approach": "Har bir mijozga individual yondashuv.",

        // ✅ Комментарии
        "comments.reviews": "Fikrlar:",
        "telegram.review": "Telegram orqali sharh qoldiring"
    }
};

// Язык по умолчанию
let currentLanguage = localStorage.getItem('lang') || new URLSearchParams(window.location.search).get('lang') || 'en';


// Обновление текста на странице
function updateLanguage(lang) {
    currentLanguage = lang;

     // Перевод текста с data-translate
    document.querySelectorAll("[data-translate]").forEach(el => {
        const key = el.getAttribute("data-translate");
        const translation = translations[currentLanguage][key];
        if (translation) {
            el.innerText = translation;
        }
    });

    // ✅ Переключаем активную кнопку языка
    document.querySelectorAll('.lang-switch').forEach(link => {
        link.classList.toggle('active', link.getAttribute('data-lang') === currentLanguage);
    });

    // ✅ Обновляем анимацию typed.js
    updateTypedText(lang);
}

// Обработчик переключения языка
document.querySelectorAll('.lang-switch').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const lang = link.getAttribute('data-lang');
        localStorage.setItem('lang', lang);
        updateLanguage(lang);
    });
});

/* Telegram Reviews — подставить default-avatar если отсутствует */
// Безопасная функция экранирования текста (чтобы защититься от XSS)
const htmlEntities = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
};

const escapeHTML = (str) => {
    if (!str) return '';
    return str.replace(/[&<>"']/g, (match) => htmlEntities[match]);
};

// Инициализация интерфейса при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    updateLanguage(currentLanguage);
    updateTypedText(currentLanguage); // запускаем typed.js с текущим языком

    // Подставляем default-avatar, если фото не загрузилось
    const reviews = document.querySelectorAll('#telegram-reviews img.avatar');
    reviews.forEach(img => {
        img.onerror = () => {
            img.onerror = null;
            img.src = '/static/images/default-avatar.png';
        };

        
        requestAnimationFrame(() => {
            if (!img.complete || img.naturalWidth === 0) {
                img.src = '/static/images/default-avatar.png';
            }
        });
    });


// получаем количество уже загруженных отзывов из data-count
    let reviewOffset = parseInt(document.getElementById('telegram-reviews').dataset.count) || 0;
    const reviewLimit = 10;

    const loadMoreBtn = document.getElementById("load-more-btn");
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener("click", async () => {
            try {
                const response = await fetch(`/api/telegram-reviews/?offset=${reviewOffset}&limit=${reviewLimit}`);
                if (!response.ok) throw new Error(`HTTP error ${response.status}`);

                const reviews = await response.json();

                const container = document.querySelector("#telegram-reviews .telegram-reviews-container");

                reviews.forEach((review) => {
                    const reviewEl = document.createElement("div");
                    reviewEl.className = "telegram-review";
                    reviewEl.innerHTML = `
                        <div class="telegram-user">
                            <img src="${review.photo_url && review.photo_url.startsWith('/') 
                                ? review.photo_url + '?v=' + Date.now() 
                                : '/static/images/default-avatar.png'}" 
                                alt="${escapeHTML(review.full_name || review.username || 'Anonymous')}" 
                                class="avatar" 
                                onerror="this.onerror=null;this.src='/static/images/default-avatar.png';">
                            <strong>${escapeHTML(review.full_name || review.username || 'Anonymous')}</strong>
                        </div>
                        <div class="telegram-rating">
                            ${'<span class="star">★</span>'.repeat(review.rating)}
                            ${'<span class="star empty">★</span>'.repeat(5 - review.rating)}
                        </div>
                        <p class="telegram-text">${escapeHTML(review.message)}</p>
                    `;
                    container.appendChild(reviewEl);
                });

                reviewOffset += reviewLimit;

                if (reviews.length < reviewLimit) {
                    document.getElementById("load-more-container").style.display = "none";
                }

            } catch (err) {
                console.error("❌ Ошибка при загрузке отзывов:", err);
                alert("Произошла ошибка при загрузке отзывов. Попробуйте позже!");
            }
        });
    }
});
