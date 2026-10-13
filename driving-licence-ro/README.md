# Permis de conducere, categoria B (proba teoretică)

Aplicația de studiu: https://claude.ai/artifact/H8A58HafBsowWXKtwqST8Q

Toate cele 12 capitole sunt gata: cartonașe cu câte o idee, test după fiecare capitol,
simulare de examen (26 de întrebări, 30 de minute) și „Greșelile mele”, unde revin
întrebările greșite până le nimerești de două ori la rând. Progresul se salvează singur.

## Cum e făcută

- `content/chNN.json`: textul capitolelor (cartonașe, rezumat, întrebări) și `content/signs.json` (81 de indicatoare desenate în SVG).
- `app/index.html`: aplicația; `app/content.js` se generează cu `python3 app/build.py`.
- `app/check.py content`: verifică structura capitolelor înainte de publicare.

## Examenul (verificat pe 9 octombrie 2026)

| | |
|---|---|
| Întrebări | 26 |
| Timp | 30 de minute |
| Promovare | minimum 22 de răspunsuri corecte (maximum 4 greșeli) |
| Variante | 3 (A, B, C); pot fi corecte una, două sau toate trei |
| Reprogramare după picare | după cel puțin 15 zile |
| Vârsta minimă | 18 ani |

O întrebare e corectă doar dacă bifezi toate variantele corecte și nimic în plus.
Poți amâna o întrebare cu „Răspunde mai târziu”.

Surse: [avocatnet.ro, septembrie 2026](https://www.avocatnet.ro/articol_72635/Permis-auto-Cum-se-poate-ob%C8%9Bine-in-2026-categoria-B.html),
[scoalarutiera.ro, formatul chestionarelor](https://www.scoalarutiera.ro/chestionare-drpciv-categoria-b).

## Capitolele (în ritmul tău; un capitol la câteva zile e suficient)

Ordinea urmează Codul rutier (OUG 195/2002) și
[cursul de legislație de pe scoalarutiera.ro](https://www.scoalarutiera.ro/curs-legislatie/codul-rutier).

1. Drumul public: elementele drumului și definițiile — [notițe](notes/01-drumul-public.md)
2. Deplasarea pe drum: folosirea benzilor, circulația pe dreapta, distanța
3. Indicatoare rutiere, pe categorii
4. Marcaje, semafoare, polițist, semnale speciale
5. Prioritatea (timp în plus, cele mai multe întrebări)
6. Intersecții, sens giratoriu, sens unic, autostradă, zone rezidențiale
7. Viteza
8. Manevre: depășire, oprire, staționare, parcare, întoarcere, mers înapoi
9. Locuri speciale: calea ferată, treceri pentru pietoni, curbe, rampe, tuneluri
10. Obligațiile șoferului: înainte și în timpul drumului, copii, accident, defecțiune, primul an
11. Sancțiuni: puncte, amenzi, alcool, infracțiuni
12. Prim ajutor, mecanică, conducere ecologică și preventivă
13. Simulări de examen (26 de întrebări, 30 de minute)

Câteva lucruri pot diferi între lege și răspunsurile din chestionarele oficiale (de exemplu la primul ajutor, unde
chestionarele pot urma ghiduri mai vechi).
Dacă vezi o diferență, merge răspunsul din chestionarul oficial.

## Notițele tale

Notițele din carte merg în `notes/`, câte un fișier pe capitol (`NN-subiect.md`).
