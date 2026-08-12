    }

    .board-nav a {
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s;
    }

    .board-nav a:hover, .board-nav a.active {
      color: var(--text-main);
    }

    /* --- CONTENEDOR PRINCIPAL --- */
    .container {
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1rem;
    }

    /* --- FORMULARIO DE NUEVO HILO --- */
    .create-thread-card {
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }

    .create-thread-card h3 {
      margin-bottom: 1rem;
      font-size: 1.1rem;
      color: var(--text-main);
    }

    .form-group {
      margin-bottom: 1rem;
    }

    .form-control {
      width: 100%;
      padding: 0.75rem 1rem;
      background-color: var(--bg-color);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }

    .form-control:focus {
      border-color: var(--accent-color);
    }

    textarea.form-control {
      resize: vertical;
      min-height: 90px;
    }

    .btn-submit {
      background-color: var(--accent-color);
      color: white;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.2s;
      width: 100%;
    }

    .btn-submit:hover {
      background-color: var(--accent-hover);
    }

    /* --- ESTILOS DE HILOS Y PUBLICACIONES --- */
    .thread {
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }

    .thread-header {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 0.85rem;
      margin-bottom: 0.75rem;
    }

    .author {
      color: var(--anon-color);
      font-weight: 700;
    }

    .post-id {
      color: var(--text-muted);
    }

    .post-time {
      color: var(--text-muted);
    }

    .thread-title {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
    }

    .thread-content {
      color: #cbd5e1;
      font-size: 0.95rem;
      white-space: pre-line;
      margin-bottom: 1rem;
    }

    .thread-image {
      max-width: 100%;
      max-height: 350px;
      border-radius: 8px;
      margin-bottom: 1rem;
      object-fit: cover;
      display: block;
    }

    /* RESPUESTAS DENTRO DEL HILO */
    .replies-container {
      margin-top: 1rem;
      padding-left: 1rem;
      border-left: 2px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .reply-card {
      background-color: rgba(15, 23, 42, 0.5);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 0.85rem;
    }

    /* BOTÓN RESP
