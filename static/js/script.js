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
let currentLanguage = localStorage.getItem('lang') || new URLSearchParams(window.location.search).get('lang') || 'ru';


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

// === Autumn FX (leaves + gentle rain) ======================================
(() => {
  const cnv = document.getElementById('autumn-canvas');
  if (!cnv) return;

  // --- config (спокойнее, чем раньше) ---
  const cfg = {
    leaves: {
      enabled: true,
      density: 0.55,        // меньше частиц
      size: [16, 40],       // px
      spin: [0.002, 0.008], // рад/мс
      wind: [0.01, 0.05],   // px/мс по X
      fall: [0.03, 0.09],   // px/мс по Y
    },
    rain: {
      enabled: true,
      density: 0.35,        // реже
      length: [6, 14],
      speed: [0.25, 0.6],   // медленнее
      slant: -0.3           // мягкий наклон
    }
  };

  // уважение к prefers-reduced-motion
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) {
    cfg.leaves.enabled = false;
    cfg.rain.enabled = false;
  }

  const ctx = cnv.getContext('2d');
  let DPR = Math.min(window.devicePixelRatio || 1, 2);
  let W = 0, H = 0, running = true;

  // --- “натуральные” листья: SVG с градиентами/прожилками ---
  const leafSVGs = [
    // клён
    `<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>
      <defs>
        <linearGradient id='g1' x1='0' x2='0' y1='0' y2='1'>
          <stop offset='0' stop-color='#ffb347'/>
          <stop offset='1' stop-color='#ff7b00'/>
        </linearGradient>
      </defs>
      <path fill='url(#g1)' d='M32 2l6 12 12-6-6 12 12 6-14 2 2 14-10-10-10 10 2-14-14-2 12-6-6-12 12 6z'/>
      <path d='M32 6v40' stroke='rgba(90,40,0,.35)' stroke-width='2'/>
      <path d='M20 24l12 8M44 24l-12 8' stroke='rgba(90,40,0,.25)' stroke-width='1.5'/>
    </svg>`,
    // жёлтый (осина/берёза)
    `<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>
      <defs>
        <radialGradient id='g2' cx='50%' cy='40%' r='60%'>
          <stop offset='0' stop-color='#ffe066'/>
          <stop offset='1' stop-color='#e6a700'/>
        </radialGradient>
      </defs>
      <path fill='url(#g2)' d='M32 6c14 0 24 12 20 24S40 58 32 58 8 46 12 30 18 6 32 6z'/>
      <path d='M32 10v40' stroke='rgba(90,40,0,.35)' stroke-width='2'/>
      <path d='M18 28l14 6M46 28l-14 6' stroke='rgba(90,40,0,.25)' stroke-width='1.3'/>
    </svg>`,
    // дуб
    `<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>
      <defs>
        <linearGradient id='g3' x1='0' x2='1' y1='0' y2='1'>
          <stop offset='0' stop-color='#ff9966'/>
          <stop offset='1' stop-color='#cc4b00'/>
        </linearGradient>
      </defs>
      <path fill='url(#g3)' d='M32 6c8 0 10 6 16 6s8 8 4 12 6 10-2 16-10-2-18 0-10 10-18 6-2-10-2-16-6-8 0-12 8 0 16-2z'/>
      <path d='M32 8v44' stroke='rgba(90,40,0,.35)' stroke-width='2'/>
      <path d='M22 22l10 6M42 22l-10 6' stroke='rgba(90,40,0,.25)' stroke-width='1.2'/>
    </svg>`
  ];

  // preload “картинок” из SVG
  const leafImgs = leafSVGs.map(s => {
    const img = new Image();
    img.src = 'data:image/svg+xml;utf8,' + encodeURIComponent(s);
    return img;
  });

  function preloadImages(imgs) {
    return Promise.all(imgs.map(img => new Promise(res => {
      if (img.complete) return res();
      img.onload = res; img.onerror = res;
    })));
  }

  // --- state ---
  let leaves = [];
  let drops  = [];

  function rnd(a,b){ return a + Math.random()*(b-a); }
  function pick(arr){ return arr[(Math.random()*arr.length)|0]; }

  function adjustCount(arr, n, factory){
    while(arr.length < n) arr.push(factory());
    while(arr.length > n) arr.pop();
  }

  function resize(){
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.floor(window.innerWidth  * DPR);
    H = Math.floor(window.innerHeight * DPR);
    cnv.width = W; cnv.height = H;
    cnv.style.width = '100%';
    cnv.style.height = '100%';

    const areaMP = (W*H)/(1000*1000); // «мегапиксели»
    const targetLeaves = (cfg.leaves.enabled ? Math.max(10, (areaMP * 90  * cfg.leaves.density)|0) : 0);
    const targetDrops  = (cfg.rain.enabled   ? Math.max(20, (areaMP * 220 * cfg.rain.density)|0) : 0);
    adjustCount(leaves, targetLeaves, makeLeaf);
    adjustCount(drops,  targetDrops,  makeDrop);
  }
  window.addEventListener('resize', resize, {passive:true});

  // --- particles factories ---
  function makeLeaf(){
    const img = pick(leafImgs);
    const s   = rnd(cfg.leaves.size[0], cfg.leaves.size[1]) * DPR;
    return {
      img,
      x: rnd(0, W), y: rnd(-H*0.5, -s),
      sx: rnd(cfg.leaves.wind[0], cfg.leaves.wind[1]) * (Math.random()<0.5 ? -1 : 1),
      sy: rnd(cfg.leaves.fall[0], cfg.leaves.fall[1]),
      a: Math.random()*Math.PI*2,
      va: rnd(cfg.leaves.spin[0], cfg.leaves.spin[1]) * (Math.random()<0.5 ? -1 : 1),
      s
    };
  }

  function makeDrop(){
    const len = rnd(cfg.rain.length[0], cfg.rain.length[1]) * DPR;
    const v   = rnd(cfg.rain.speed[0], cfg.rain.speed[1]);
    const vx  = v * cfg.rain.slant * DPR;
    const vy  = v * 2.0 * DPR;
    return {
      x: rnd(0, W), y: rnd(-H*0.3, 0),
      vx, vy, len
    };
  }

  // --- loop ---
  let last = performance.now();
  function tick(t){
    if (!running) return;
    const dt = Math.min(40, t - last);
    last = t;

    ctx.clearRect(0,0,W,H);

    // rain
    if (cfg.rain.enabled){
      ctx.strokeStyle = 'rgba(255,255,255,0.12)'; // мягче
      ctx.lineWidth = 1 * DPR;
      ctx.beginPath();
      for (let d of drops){
        d.x += d.vx*dt; d.y += d.vy*dt;
        if (d.y > H || d.x < -50 || d.x > W+50){
          Object.assign(d, makeDrop()); d.y = -5;
        }
        ctx.moveTo(d.x, d.y);
        ctx.lineTo(d.x - cfg.rain.slant*d.len*1.2, d.y + d.len);
      }
      ctx.stroke();
    }

    // leaves
    if (cfg.leaves.enabled){
      for (let p of leaves){
        p.x += p.sx*dt; p.y += p.sy*dt; p.a += p.va*dt;
        if (p.y > H+40 || p.x < -80 || p.x > W+80){
          Object.assign(p, makeLeaf()); p.y = -20;
        }
        const s = p.s;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(Math.sin(p.a) * 0.7);
        ctx.drawImage(p.img, -s/2, -s/2, s, s);
        ctx.restore();
      }
    }

    // простой “адаптер” производительности
    if (dt > 30){
      cfg.leaves.density = Math.max(0.3, cfg.leaves.density - 0.05);
      cfg.rain.density   = Math.max(0.3, cfg.rain.density   - 0.05);
      resize();
    }

    requestAnimationFrame(tick);
  }

  // pause on background tab
  document.addEventListener('visibilitychange', () => {
    running = (document.visibilityState === 'visible');
    if (running){ last = performance.now(); requestAnimationFrame(tick); }
  });

  // toggle button (optional)
  const btn = document.getElementById('toggle-autumn');
  if (btn){
    btn.addEventListener('click', () => {
      const enable = !(cfg.leaves.enabled || cfg.rain.enabled);
      cfg.leaves.enabled = enable;
      cfg.rain.enabled   = enable;
      cnv.style.display  = enable ? 'block' : 'none';
      if (enable) { resize(); }
    });
  }

  // start after images are ready
  preloadImages(leafImgs).then(() => {
    resize();
    requestAnimationFrame(tick);
  });
})();

// === Realtime Weather (Open-Meteo) ==========================
(function () {
  const host = document.getElementById('weather');
  if (!host) return;

  // Город по умолчанию (Ташкент; можно поменять)
  const FALLBACK = { name: {ru:'Ташкент', en:'Tashkent', uz:'Toshkent'}, lat:41.3111, lon:69.2797 };

  const t = (lang, dict) => dict[lang] ?? dict.en;
  const lang = (document.documentElement.getAttribute('lang') || 'en').slice(0,2);

  // Простая карта погодных кодов Open-Meteo → эмодзи/иконка
  const codeIcon = (code) => {
    // https://open-meteo.com/en/docs#weathervariables → weathercode
    if ([0].includes(code)) return '☀️';
    if ([1].includes(code)) return '🌤️';
    if ([2].includes(code)) return '⛅';
    if ([3].includes(code)) return '☁️';
    if ([45,48].includes(code)) return '🌫️';
    if ([51,53,55,61,63,65,80,81,82].includes(code)) return '🌧️';
    if ([56,57,66,67,85,86,71,73,75,77].includes(code)) return '❄️';
    if ([95,96,99].includes(code)) return '⛈️';
    return '🌡️';
  };

  const unitSymbol = (lang) => '°C'; // при желании можно сделать переключатель C/F

  const cacheKey = (coords) => `weather:${coords.lat.toFixed(2)},${coords.lon.toFixed(2)}`;
  const loadFromCache = (key) => {
    try {
      const raw = localStorage.getItem(key);
      if (!raw) return null;
      const obj = JSON.parse(raw);
      if (Date.now() - obj.ts > 10 * 60 * 1000) return null; // 10 минут
      return obj.data;
    } catch { return null; }
  };
  const saveToCache = (key, data) => {
    try { localStorage.setItem(key, JSON.stringify({ ts: Date.now(), data })); } catch {}
  };

  const render = ({ placeName, temp, code }) => {
    host.innerHTML = `
      <span class="w-icon">${codeIcon(code)}</span>
      <span class="w-temp">${Math.round(temp)}${unitSymbol(lang)}</span>
      <span class="w-place">${placeName}</span>
    `;
  };
  const renderError = () => {
    host.innerHTML = `<span class="w-icon">⚠️</span><span>${t(lang, {
      ru: 'Погода недоступна', en: 'Weather unavailable', uz: 'Ob-havo mavjud emas'
    })}</span>`;
  };

  async function fetchWeather(coords, placeName) {
    const key = cacheKey(coords);
    const cached = loadFromCache(key);
    if (cached) {
      render({ placeName, temp: cached.temperature, code: cached.weathercode });
      return;
    }
    const url = new URL('https://api.open-meteo.com/v1/forecast');
    url.searchParams.set('latitude', coords.lat);
    url.searchParams.set('longitude', coords.lon);
    url.searchParams.set('current_weather', 'true');
    url.searchParams.set('timezone', 'auto');

    try {
      const res = await fetch(url.toString(), { cache: 'no-store' });
      if (!res.ok) throw new Error(res.status);
      const data = await res.json();
      const cw = data.current_weather;
      if (!cw) throw new Error('no current_weather');
      saveToCache(key, cw);
      render({ placeName, temp: cw.temperature, code: cw.weathercode });
    } catch (e) {
      renderError();
    }
  }

  function useFallback() {
    host.querySelector('.w-loading')?.remove();
    fetchWeather({ lat: FALLBACK.lat, lon: FALLBACK.lon }, t(lang, FALLBACK.name));
  }

  // 1) Пытаемся взять геолокацию пользователя (с разрешения)
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const coords = { lat: pos.coords.latitude, lon: pos.coords.longitude };
        fetchWeather(coords, t(lang, { ru:'Ваше местоположение', en:'Your location', uz:'Sizning joylashuvingiz' }));
      },
      useFallback,
      { enableHighAccuracy: false, timeout: 5000, maximumAge: 5*60*1000 }
    );
  } else {
    useFallback();
  }
})();
