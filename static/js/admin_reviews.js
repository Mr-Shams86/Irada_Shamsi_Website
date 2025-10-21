// Автозагрузка при входе на страницу
document.addEventListener("DOMContentLoaded", fetchAdminReviews);

// Достаём токен модератора из query (?token=...)
const urlParams = new URLSearchParams(window.location.search);
const token = urlParams.get("token");

// ---- Настройки / хелперы -------
const DEFAULT_AVATAR = '/static/images/default-avatar.2025-10-17.png';

function isHttp(url) {
  return typeof url === 'string' && /^https?:\/\//i.test(url);
}
function isLocal(url) {
  return typeof url === 'string' && url.startsWith('/');
}
function escapeHTML(s = '') {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// ---- Загрузка списка отзывов -----------
async function fetchAdminReviews() {
  const container = document.getElementById("admin-reviews-container");
  if (!container) return;

  try {
    const res = await fetch(`/admin/reviews/list?token=${encodeURIComponent(token)}`);
    if (!res.ok) throw new Error("Ошибка загрузки");

    const reviews = await res.json();

    if (!reviews.length) {
      container.innerHTML = '<p style="color:#999">Нет отзывов для модерации 😌</p>';
      return;
    }

    container.innerHTML = "";
    reviews.forEach(review => {
      // --- выбор src для аватарки
      let avatarSrc = DEFAULT_AVATAR;
      if (isLocal(review.photo_url)) {
        // свежие локальные авы — с bust, чтобы не прилипал кеш
        avatarSrc = `${review.photo_url}?v=${Date.now()}`;
      } else if (isHttp(review.photo_url)) {
        // внешние URL, если когда-то были
        avatarSrc = review.photo_url;
      }

      // --- безопасные тексты
      const displayName = escapeHTML(review.full_name || review.username || 'Аноним');
      const messageSafe = escapeHTML(review.message);

      // --- разметка карточки
      const div = document.createElement("div");
      div.classList.add("admin-review");
      
      div.innerHTML = `
        <div class="telegram-user">
          <img
            src="${avatarSrc}"
            alt="${displayName}"
            class="avatar"
            loading="lazy"
            onerror="this.onerror=null;this.src='${DEFAULT_AVATAR}'"
          >
          <strong>${displayName}</strong>
        </div>

        <div class="telegram-rating">Оценка: ${review.rating} ⭐</div>
        <p class="telegram-text">${messageSafe}</p>

        <div class="moderation-buttons">
          <button onclick="approveReview(${review.id})" class="btn-approve">✅ Одобрить</button>
          <button onclick="deleteReview(${review.id})" class="btn-delete">🗑️ Удалить</button>
        </div>
      `;

      container.appendChild(div);
    });
  } catch (err) {
    console.error('[AdminReviews] load failed:', err);
    container.innerHTML = '<p style="color:red">Ошибка загрузки отзывов</p>';
  }
}

// ---- Действия модерации -----------------------------------------------------
async function approveReview(id) {
  if (!confirm('Одобрить отзыв?')) return;
  await fetch(`/admin/reviews/${id}/approve?token=${encodeURIComponent(token)}`, {
    method: 'POST',
  });
  fetchAdminReviews();
}

async function deleteReview(id) {
  if (!confirm('Удалить отзыв?')) return;
  await fetch(`/admin/reviews/${id}?token=${encodeURIComponent(token)}`, {
    method: 'DELETE',
  });
  fetchAdminReviews();
}

// Экспортируем в глобальную область, чтобы кнопки могли вызывать
window.approveReview = approveReview;
window.deleteReview = deleteReview;

