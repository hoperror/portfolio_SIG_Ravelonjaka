#import "@preview/nabcv:0.1.0": cv

#let cd = toml("cv.toml").cv

// Corriger les puces de liste
#set list(marker: [•])

#show: cv.with(
  name: cd.name,
  headline: cd.at("headline", default: none),
  location: cd.at("location", default: none),
  keywords: cd.at("keywords", default: none),
  email: cd.at("email", default: none),
  phone: cd.at("phone", default: none),
  address: cd.at("address", default: none),
  profiles: cd.at("profiles", default: none),
  profiles-config: (
    LinkedIn: (icon: "linkedin", url-base: "https://linkedin.com/in/"),
    GitHub: (icon: "github", url-base: "https://github.com/"),
    Portfolio: (icon: "globe", url-base: "https://hoperror.github.io/portfolio_SIG_Ravelonjaka/#"),
  ),
  summary: cd.at("summary", default: none),
  experience: cd.at("experience", default: none),
  education: cd.at("education", default: none),
  skills: cd.at("skills", default: none),
  values: cd.at("values", default: none),
  hobbies: cd.at("hobbies", default: none),
  sidebar-sections: ("contact", "skills", "values", "hobbies"),
  main-sections: ("summary", "experience", "education"),
  section-titles: (
    summary: "PROFIL",
    experience: "EXPÉRIENCES PROFESSIONNELLES",
    education: "FORMATION",
    skills: "COMPÉTENCES",
    values: "QUALITÉS",
    hobbies: "CENTRES D'INTÉRÊT",
    contact: "CONTACT",
  ),
  section-icons: (
    summary: "id-card",
    experience: "suitcase",
    education: "graduation-cap",
    skills: "wrench",
    values: "check-circle",
    hobbies: "futbol",
    contact: "envelope",
  ),
)