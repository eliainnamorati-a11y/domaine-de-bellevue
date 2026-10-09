/**
 * Domaine de Bellevue - Main Interactive Script
 * High-End Luxury Real Estate Experience
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Language Dictionary (FR / EN)
  const translations = {
    fr: {
      nav_project: "Le Projet",
      nav_arch: "Architecture",
      nav_villas: "Les Villas",
      nav_custom: "Personnalisation",
      nav_situation: "Situation",
      nav_contact: "Contact",
      btn_inquire: "Prendre Rendez-vous",
      hero_badge: "Dernières 3 Opportunités • Disponibilité 2027",
      hero_title_1: "L'Équilibre Parfait",
      hero_title_2: "entre Style et Sérénité",
      hero_sub: "Un ensemble d'exception sur les hauteurs paisibles de Trélex, près de Nyon et Genève. Seulement 3 villas de prestige encore disponibles.",
      hero_status_sold: "5 Villas Déjà Vendues",
      hero_status_avail: "Villas 1, 2 & 3 Disponibles",
      hero_cta_villas: "Découvrir les 3 Dernières Villas",
      hero_cta_custom: "Personnaliser votre Villa",
      banner_tag: "Opportunité Rare",
      banner_text: "Phase initiale de construction : Personnalisez librement vos aménagements et finitions intérieures.",
      banner_cta: "Voir les options sur mesure →",
      
      proj_label: "LE PROJET",
      proj_heading: "Un domaine pensé pour vous",
      proj_p1: "À une adresse privilégiée, sur les hauteurs paisibles de Trélex, se déploie un ensemble rare de huit villas d’exception. Conçu comme un véritable domaine privé, ce projet allie raffinement, discrétion et confort haut de gamme.",
      proj_p2: "Nichées dans un écrin de verdure, chaque bien est conçu pour un art de vivre contemporain : volumes lumineux, terrasses privées spacieuses et modularité intelligente.",
      
      sig_label: "COLLECTION SIGNATURE",
      sig_heading: "Pourquoi les Villas 1, 2 et 3 sont les joyaux du Domaine",
      sig_desc: "Dernières disponibilités du projet, ces 3 villas occupent les parcelles les plus prisées et spacieuses du domaine, justifiant leur standing supérieur.",
      
      custom_label: "SUR MESURE",
      custom_heading: "Personnalisation Intégrale en Phase Initiale",
      custom_desc: "La construction étant dans sa phase initiale, vous bénéficiez du privilège rare de redéfinir la distribution des pièces et de choisir chaque matériau noble avec les architectes.",

      villas_label: "TABLEAU DES LOTS",
      villas_heading: "Disponibilités & Masterplan Interactif",
      villas_desc: "Survolez chaque lot pour visualiser son implantation sur le domaine de Bellevue.",

      life_label: "LIFESTYLE",
      life_heading: "L'Art de Vivre sur la Côte",
      
      sit_label: "EMPLACEMENT STRATÉGIQUE",
      sit_heading: "Trélex & la Région Lémanique",
      
      dl_label: "DOCUMENTATION",
      dl_heading: "Téléchargez le Dossier Officiel",

      contact_label: "CONTACT PRIVILÉGIÉ",
      contact_heading: "Conseil & Vente Personnalisés"
    },
    en: {
      nav_project: "The Project",
      nav_arch: "Architecture",
      nav_villas: "The Villas",
      nav_custom: "Customization",
      nav_situation: "Location",
      nav_contact: "Contact",
      btn_inquire: "Book a Viewing",
      hero_badge: "Final 3 Opportunities • Delivery 2027",
      hero_title_1: "The Perfect Balance",
      hero_title_2: "between Style and Serenity",
      hero_sub: "A rare private estate in the tranquil heights of Trélex, close to Nyon and Geneva. Only 3 prime luxury villas remain available.",
      hero_status_sold: "5 Villas Already Sold",
      hero_status_avail: "Villas 1, 2 & 3 Available",
      hero_cta_villas: "Explore the Final 3 Villas",
      hero_cta_custom: "Customize Your Villa",
      banner_tag: "Rare Opportunity",
      banner_text: "Early construction phase: Freely tailor your interior layout and high-end finishes with the architect.",
      banner_cta: "Discover bespoke options →",

      proj_label: "THE PROJECT",
      proj_heading: "A Sanctuary Designed for You",
      proj_p1: "At an exclusive address on the peaceful heights of Trélex, an exquisite enclave of eight bespoke villas is coming to life. Conceived as a secure private estate, it embodies discretion and world-class luxury.",
      proj_p2: "Surrounded by nature, each home is crafted for contemporary living: generous double-height volumes, panoramic terraces, and intuitive modularity.",

      sig_label: "SIGNATURE COLLECTION",
      sig_heading: "Why Villas 1, 2 and 3 are the Crown Jewels",
      sig_desc: "The final available properties occupy the estate's largest and most elevated parcels, justifying their premier positioning.",

      custom_label: "BESPOKE DESIGN",
      custom_heading: "Complete Tailoring in Early Building Phase",
      custom_desc: "Because construction is in its initial stage, you have the rare privilege to reconfigure floor plans and hand-pick every noble material alongside the architect.",

      villas_label: "LOT SELECTOR",
      villas_heading: "Availability & Interactive Masterplan",
      villas_desc: "Hover over each lot to view its position and sunlight exposure across the estate.",

      life_label: "LIFESTYLE",
      life_heading: "The Art of Living on the Swiss Riviera",

      sit_label: "PRIME LOCATION",
      sit_heading: "Trélex & the Greater Lake Geneva Area",

      dl_label: "DOCUMENTATION",
      dl_heading: "Download Official Brochures & Plans",

      contact_label: "EXCLUSIVE ADVISORY",
      contact_heading: "Personalized Sales & Advisory"
    }
  };

  let currentLang = "fr";

  // 2. Language Switcher
  const langBtns = document.querySelectorAll(".lang-btn");
  function setLanguage(lang) {
    currentLang = lang;
    langBtns.forEach(btn => {
      btn.classList.toggle("active", btn.dataset.lang === lang);
    });

    document.querySelectorAll("[data-i18n]").forEach(el => {
      const key = el.getAttribute("data-i18n");
      if (translations[lang] && translations[lang][key]) {
        el.textContent = translations[lang][key];
      }
    });
  }

  langBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      setLanguage(btn.dataset.lang);
    });
  });

  // 3. Header Shrink on Scroll
  const header = document.getElementById("site-header");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("shrink");
    } else {
      header.classList.remove("shrink");
    }
  });

  // 4. Hero Slideshow
  const heroSlides = document.querySelectorAll(".hero-slide");
  let heroIndex = 0;
  if (heroSlides.length > 0) {
    setInterval(() => {
      heroSlides[heroIndex].classList.remove("active");
      heroIndex = (heroIndex + 1) % heroSlides.length;
      heroSlides[heroIndex].classList.add("active");
    }, 6000);
  }

  // 5. Interactive Lot Table & Plan Image Swapping
  const tableRows = document.querySelectorAll(".interactive-table tbody tr");
  const planImages = document.querySelectorAll(".image-display img");
  let currentPinnedImg = 0;

  function showPlanImage(index) {
    planImages.forEach((img, i) => {
      img.classList.toggle("active", i === index);
    });
  }

  tableRows.forEach(row => {
    const imgIndex = parseInt(row.dataset.img, 10);
    
    row.addEventListener("mouseenter", () => {
      showPlanImage(imgIndex);
    });

    row.addEventListener("mouseleave", () => {
      showPlanImage(currentPinnedImg);
    });

    row.addEventListener("click", () => {
      currentPinnedImg = imgIndex;
      showPlanImage(imgIndex);
      
      // If clicking villa 1, 2, or 3, highlight its showcase card smoothly
      if (imgIndex >= 1 && imgIndex <= 3) {
        const targetCard = document.getElementById(`villa-card-${imgIndex}`);
        if (targetCard) {
          targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
          targetCard.classList.add("featured");
          setTimeout(() => {
            if (imgIndex !== 1) targetCard.classList.remove("featured");
          }, 2500);
        }
      }
    });
  });

  // 6. Interactive Customization Configurator
  const configPills = document.querySelectorAll(".config-pill");
  const summarySelections = {
    villa: "Villa 1 (Belvédère)",
    layout: "4 Chambres + Bureau Télétravail",
    basement: "Espace Wellness, Sauna & Fitness",
    kitchen: "Îlot Central Marbre Dekton & Miele",
    outdoor: "Piscine Chauffée (8x4m) & Terrasse"
  };

  configPills.forEach(pill => {
    pill.addEventListener("click", () => {
      const step = pill.dataset.step;
      const value = pill.dataset.value;
      const label = pill.textContent.trim();

      // Deactivate siblings in the same step
      const siblings = document.querySelectorAll(`.config-pill[data-step="${step}"]`);
      siblings.forEach(s => s.classList.remove("active"));
      pill.classList.add("active");

      // Update internal state
      summarySelections[step] = label;

      // Update UI summary element
      const summaryEl = document.getElementById(`summary-${step}`);
      if (summaryEl) {
        summaryEl.textContent = label;
      }
    });
  });

  // Configurator Action Button
  const btnConfigDossier = document.getElementById("btn-config-dossier");
  if (btnConfigDossier) {
    btnConfigDossier.addEventListener("click", () => {
      const contactSection = document.getElementById("contact");
      const messageField = document.getElementById("contact-message");
      const villaSelect = document.getElementById("contact-villa");

      // Pre-select villa
      if (villaSelect) {
        if (summarySelections.villa.includes("1")) villaSelect.value = "1";
        else if (summarySelections.villa.includes("2")) villaSelect.value = "2";
        else if (summarySelections.villa.includes("3")) villaSelect.value = "3";
      }

      // Pre-fill tailored message
      if (messageField) {
        messageField.value = `Bonjour,\n\nJe suis particulièrement intéressé(e) par la ${summarySelections.villa}.\nJe souhaite explorer les options de personnalisation suivantes :\n- Disposition : ${summarySelections.layout}\n- Aménagement Sous-sol : ${summarySelections.basement}\n- Style Cuisine : ${summarySelections.kitchen}\n- Aménagements Extérieurs : ${summarySelections.outdoor}\n\nMerci de bien vouloir me transmettre le dossier architectural complet et me contacter pour organiser un rendez-vous.`;
      }

      if (contactSection) {
        contactSection.scrollIntoView({ behavior: "smooth" });
      }
    });
  }

  // 7. Lifestyle Carousel Navigation
  const scrollContainer = document.querySelector(".scroll-container");
  const btnLeft = document.querySelector(".scroll-btn.left");
  const btnRight = document.querySelector(".scroll-btn.right");

  if (scrollContainer && btnLeft && btnRight) {
    const scrollAmount = 400;

    btnLeft.addEventListener("click", () => {
      scrollContainer.scrollBy({ left: -scrollAmount, behavior: "smooth" });
    });

    btnRight.addEventListener("click", () => {
      scrollContainer.scrollBy({ left: scrollAmount, behavior: "smooth" });
    });
  }

  // 8. Villa Details Modal
  const villaModalsData = {
    1: {
      title: "Villa 1 – La Parcelle Belvédère (Lot 01)",
      tagline: "Le plus grand jardin privé du Domaine (952 m²) avec vue dominante sur le Léman",
      surface_total: "372 m² SBP",
      surface_hab: "198 m² Habitable",
      garden: "952 m² Jardin",
      description: "Véritable pièce maîtresse du domaine, la Villa 1 bénéficie d'une parcelle exceptionnelle de près de 1'000 m². Sa situation en hauteur lui confère une intimité rare, sans vis-à-vis, avec une perspective dégagée sur les Alpes et le lac Léman. Idéale pour l'implantation d'une piscine creusée et de vastes terrasses ensoleillées.",
      features: [
        "Jardin monumental de 952 m² : le plus étendu de tout le projet",
        "Position dominante en proue du domaine offrant une intimité totale",
        "Espace extérieur propice à la construction d'une piscine chauffée (faisabilité étudiée)",
        "Séjour traversant avec baies vitrées coulissantes à galandage",
        "4 à 5 suites parentales configurables en phase initiale",
        "Sous-sol complet de plus de 100 m² (salle de sport, spa, carnotzet ou cinéma)"
      ],
      pdf: "#contact"
    },
    2: {
      title: "Villa 2 – Le Volume Panorama (Lot 02)",
      tagline: "La plus grande surface brute de plancher du projet (376 m²) avec orientation Sud / Sud-Ouest",
      surface_total: "376 m² SBP",
      surface_hab: "201 m² Habitable",
      garden: "498 m² Jardin",
      description: "La Villa 2 offre les volumes intérieurs les plus majestueux de l'ensemble du domaine. Conçue pour sublimer la lumière naturelle tout au long de la journée, elle dispose d'une triple exposition et d'espaces de vie exceptionnellement généreux avec de grandes ouvertures sur la terrasse et le jardin paysager.",
      features: [
        "Plus vaste surface construite du domaine : 376 m² de surface brute",
        "Ensoleillement maximal Sud et Sud-Ouest du matin au coucher du soleil",
        "Séjour cathédrale ou double hauteur réalisable selon vos souhaits actuels",
        "Terrasse principale suspendue de plus de 55 m²",
        "Master suite avec dressing sur mesure de 24 m² et salle de bain balnéo",
        "Accès direct au sous-sol aménagé avec lumière naturelle par cours anglaises"
      ],
      pdf: "#contact"
    },
    3: {
      title: "Villa 3 – L'Écrin Sérénité (Lot 03)",
      tagline: "Terrain généreux de 530 m² adossé à un écrin de verdure préservé",
      surface_total: "370 m² SBP",
      surface_hab: "200 m² Habitable",
      garden: "530 m² Jardin",
      description: "Nichée en bordure de zone végétale protégée, la Villa 3 allie élégance architecturale et calme absolu. Son jardin de 530 m² propose un équilibre parfait entre facilité d'entretien et espace de jeux ou de détente familiale sous les arbres majestueux de Trélex.",
      features: [
        "Parcelle généreuse de 530 m² protégée par un cordon boisé",
        "Atmosphère paisible et intimiste à l'écart de tout passage",
        "Distribution familiale optimale avec modularité intégrale de l'étage",
        "Espace de vie ouvert de plus de 65 m² avec cuisine d'architecte",
        "Possibilité d'aménager un carnotzet vaudois traditionnel ou une cave à vin de dégustation",
        "Finitions de haute facture personnalisables à 100% avec les architectes"
      ],
      pdf: "#contact"
    }
  };

  const modalOverlay = document.getElementById("villa-modal");
  const modalBody = document.getElementById("modal-body-content");
  const modalClose = document.getElementById("modal-close");

  window.openVillaModal = function(lotId) {
    const data = villaModalsData[lotId];
    if (!data) return;

    modalBody.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
        <div>
          <span style="font-family:var(--font-title); font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--color-gold); font-weight:700;">COLLECTION SIGNATURE</span>
          <h2 style="font-family:var(--font-serif); font-size:2rem; color:var(--color-primary-dark); margin:4px 0 8px;">${data.title}</h2>
          <p style="font-size:0.95rem; color:var(--color-gold-light); font-weight:500;">${data.tagline}</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; background:var(--color-bg-alt); padding:16px; border-radius:6px; margin:20px 0; text-align:center;">
        <div>
          <strong style="display:block; font-size:1.15rem; color:var(--color-primary-dark);">${data.surface_total}</strong>
          <span style="font-size:0.7rem; text-transform:uppercase; color:var(--color-text-subtle);">Surface Totale</span>
        </div>
        <div>
          <strong style="display:block; font-size:1.15rem; color:var(--color-primary-dark);">${data.surface_hab}</strong>
          <span style="font-size:0.7rem; text-transform:uppercase; color:var(--color-text-subtle);">Habitable</span>
        </div>
        <div>
          <strong style="display:block; font-size:1.15rem; color:var(--color-primary-dark);">${data.garden}</strong>
          <span style="font-size:0.7rem; text-transform:uppercase; color:var(--color-text-subtle);">Parcelle / Jardin</span>
        </div>
      </div>

      <p style="font-size:0.95rem; line-height:1.75; color:var(--color-text-muted); margin-bottom:24px;">${data.description}</p>

      <h4 style="font-family:var(--font-title); font-size:0.9rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--color-primary-dark); margin-bottom:12px;">Points Forts & Personnalisations Clés :</h4>
      <ul style="margin-bottom:28px;">
        ${data.features.map(f => `<li style="font-size:0.88rem; color:var(--color-text-muted); margin-bottom:8px; padding-left:18px; position:relative;"><span style="position:absolute; left:0; color:var(--color-gold);">✓</span> ${f}</li>`).join("")}
      </ul>

      <div style="background:var(--color-bg); border-left:3px solid var(--color-gold); padding:16px; margin-bottom:24px;">
        <strong style="font-size:0.85rem; color:var(--color-primary-dark); display:block; margin-bottom:4px;">Phase Initiale de Construction :</strong>
        <p style="font-size:0.8rem; color:var(--color-text-muted); margin:0;">Vous pouvez actuellement réagencer les pièces intérieures, déplacer les cloisons et choisir l'ensemble des matériaux chez nos fournisseurs partenaires.</p>
      </div>

      <div style="display:flex; gap:14px; flex-wrap:wrap;">
        <a href="${data.pdf}" target="_blank" class="btn-primary" style="padding:12px 24px; font-size:0.8rem;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Plans sur demande
        </a>
        <button onclick="selectVillaAndContact('${lotId}')" class="btn-outline" style="color:var(--color-primary-dark); border-color:var(--color-primary-dark); padding:12px 24px; font-size:0.8rem;">
          Organiser un Rendez-vous Privé
        </button>
      </div>
    `;

    modalOverlay.classList.add("active");
  };

  if (modalClose) {
    modalClose.addEventListener("click", () => {
      modalOverlay.classList.remove("active");
    });
  }

  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) {
      modalOverlay.classList.remove("active");
    }
  });

  window.selectVillaAndContact = function(lotId) {
    modalOverlay.classList.remove("active");
    const contactSection = document.getElementById("contact");
    const villaSelect = document.getElementById("contact-villa");
    if (villaSelect) villaSelect.value = lotId;
    if (contactSection) contactSection.scrollIntoView({ behavior: "smooth" });
  };

  // 9. Mobile Menu
  const menuToggle = document.getElementById("menu-toggle");
  const mobileLinks = document.querySelectorAll(".mobile-nav-links a");

  if (menuToggle) {
    menuToggle.addEventListener("click", () => {
      document.body.classList.toggle("menu-open");
    });
  }

  mobileLinks.forEach(link => {
    link.addEventListener("click", () => {
      document.body.classList.remove("menu-open");
    });
  });

  // 11. Villa Multi-View Image Galleries
  const galleryContainers = document.querySelectorAll(".villa-gallery-container");
  galleryContainers.forEach(container => {
    const mainImages = container.querySelectorAll(".gallery-main-img");
    const thumbs = container.querySelectorAll(".gallery-thumb");
    const prevBtn = container.querySelector(".gallery-nav-btn.prev");
    const nextBtn = container.querySelector(".gallery-nav-btn.next");
    let activeIdx = 0;

    function switchView(index) {
      if (mainImages.length === 0) return;
      activeIdx = (index + mainImages.length) % mainImages.length;
      mainImages.forEach((img, i) => {
        img.classList.toggle("active", i === activeIdx);
      });
      thumbs.forEach((thumb, i) => {
        thumb.classList.toggle("active", i === activeIdx);
      });
    }

    thumbs.forEach(thumb => {
      thumb.addEventListener("click", (e) => {
        e.stopPropagation();
        const idx = parseInt(thumb.dataset.index, 10);
        switchView(idx);
      });
    });

    if (prevBtn) {
      prevBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        switchView(activeIdx - 1);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        switchView(activeIdx + 1);
      });
    }
  });
});
