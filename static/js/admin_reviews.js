// Автоматически загружаем отзывы при загрузке страницы
document.addEventListener("DOMContentLoaded", fetchAdminReviews);

const urlParams = new URLSearchParams(window.location.search);
const token = urlParams.get("token");

async function fetchAdminReviews() {
  const container = document.getElementById("admin-reviews-container");
  try {
    const res = await fetch(`/admin/reviews/list?token=${token}`);
    if (!res.ok) throw new Error("Ошибка загрузки");
    const reviews = await res.json();

    if (!reviews.length) {
      container.innerHTML = '<p style="color:#999">Нет отзывов для модерации 😌</p>';
      return;
    }

    container.innerHTML = "";
    reviews.forEach(review => {
      console.log(">> review.photo_url", review.photo_url); // 👈 Добавь это
      const div = document.createElement("div");
      div.classList.add("admin-review");
      div.innerHTML = `
        <div class="telegram-user">
          <img src="${review.photo_url && review.photo_url.startsWith('/') ? review.photo_url : '/static/images/default-avatar.png'}" class="avatar" onerror="this.onerror=null;this.src='/static/images/default-avatar.png';">
          <strong>${review.full_name || review.username || 'Аноним'}</strong>
        </div>
        <div class="telegram-rating">Оценка: ${review.rating} ⭐</div>
        <p class="telegram-text">${review.message}</p>
        <div class="moderation-buttons">
          <button onclick="approveReview(${review.id})" class="btn-approve">✅ Одобрить</button>
          <button onclick="deleteReview(${review.id})" class="btn-delete">🗑 Удалить</button>
        </div>`;
      container.appendChild(div);
    });
  } catch (err) {
    container.innerHTML = '<p style="color:red">Ошибка загрузки отзывов</p>';
  }
}

async function approveReview(id) {
  if (!confirm("Одобрить отзыв?")) return;
  await fetch(`/admin/reviews/${id}/approve?token=${token}`, {
    method: "POST"
  });
  fetchAdminReviews();
}

async function deleteReview(id) {
  if (!confirm("Удалить отзыв?")) return;
  await fetch(`/admin/reviews/${id}?token=${token}`, {
    method: "DELETE"
  });
  fetchAdminReviews();
}



