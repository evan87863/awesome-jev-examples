# Awesome Jev Examples

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · **Español**

> Descubre qué se construye con Jev, cómo funciona y dónde aprender más.

Índice seleccionado de recursos para **[Jev de TypeSafe AI](https://docs.typesafe.ai/introduction)**, un modelo de decisiones que responde preguntas Choice, Score y Noul sobre un estado proporcionado. Proyecto comunitario independiente, sin afiliación con TypeSafe AI.

[Primeros pasos](docs/START-HERE.es.md) · [Todos los detalles](catalog/DETAILS.es.md) · [X / YouTube](catalog/MEDIA.es.md) · [Contribuir (inglés)](CONTRIBUTING.md)

**72 recursos:** 46 proyectos con código o SDK, 25 guías, patrones y referencias oficiales, y 1 informe del equipo desarrollador. Otros **28 enlaces de X / YouTube** pendientes de revisión. Revisión inicial: 2026-09-19.

Revisado significa que se leyó la fuente indicada, no que se ejecutó o auditó el proyecto. No hemos reproducido ningún ejemplo. Dos páginas oficiales se recuperaron parcialmente y están señaladas. No verificamos de forma independiente las cifras de rendimiento de los autores.

## Empieza por aquí

- **[Inicio rápido](https://docs.typesafe.ai/introduction/quickstart)** — Crea una primera solicitud tipada en el Playground o con el SDK. [Ver detalles](catalog/DETAILS.es.md#official-quickstart)
- **[Jev Ultrafast](https://github.com/browser-use/jev-ultrafast)** — Elige conjuntamente una acción del navegador y su destino en una tabla dinámica de elementos. [Ver detalles](catalog/DETAILS.es.md#browser-use--jev-ultrafast)
- **[Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review)** — Revisa cambios o repositorios por etapas: riesgos, selección de pruebas y gravedad. [Ver detalles](catalog/DETAILS.es.md#devagrawal09--jev-review)
- **[Kill My Idea](https://github.com/monteduro/killmyidea)** — Evalúa una idea de negocio con preguntas paralelas y combina puntuaciones en un veredicto fijo. [Ver detalles](catalog/DETAILS.es.md#monteduro--killmyidea)
- **[neo4jev](https://github.com/jexp/neo4jev)** — Elige la siguiente relación del grafo y comprueba si se alcanzó la meta en una misma llamada. [Ver detalles](catalog/DETAILS.es.md#jexp--neo4jev)
- **[Janus](https://github.com/FirasSX914/Janus)** — Mide cuándo derivar tareas entre modelos pequeños y grandes, y cuándo no conviene hacerlo. [Ver detalles](catalog/DETAILS.es.md#firassx914--janus)
- **[Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab)** — Experimentos de ajedrez comparan Jev solo, filtros tácticos y ayuda de Stockfish. [Ver detalles](catalog/DETAILS.es.md#denikuchero--jev-chess-lab)

## Explora por uso

- [Guías oficiales y SDK](#official) (26)
- [Navegador, escritorio y móvil](#browser) (8)
- [Agentes de programación y MCP](#agents) (8)
- [Enrutamiento de modelos](#routing) (2)
- [Moderación, reglas y controles de seguridad](#safety) (5)
- [Búsqueda y grafos de conocimiento](#retrieval) (1)
- [Datos y observabilidad](#data) (4)
- [Automatización cotidiana y hogar inteligente](#automation) (2)
- [Aplicaciones y herramientas de contenido](#applications) (4)
- [Juegos y simulaciones](#games) (6)
- [Evaluación y calibración](#evaluation) (5)
- [Experimentos con los límites](#experiments) (1)

<a id="official"></a>

## Guías oficiales y SDK

| Recurso | Resumen y detalles |
| --- | --- |
| [SDK oficial de Python](https://github.com/typesafe-ai/typesafe-sdk-python) | Cliente oficial de Python con un ejemplo mínimo de clasificación de tickets. [Ver detalles](catalog/DETAILS.es.md#typesafe-ai--typesafe-sdk-python) |
| [Inicio rápido](https://docs.typesafe.ai/introduction/quickstart) | Crea una primera solicitud tipada en el Playground o con el SDK. [Ver detalles](catalog/DETAILS.es.md#official-quickstart) |
| [Evaluación especulativa en paralelo](https://docs.typesafe.ai/patterns/fan-out) | Pregunta por varias ramas a la vez y selecciona las respuestas pertinentes mediante código. [Ver detalles](catalog/DETAILS.es.md#official-fan-out) |
| [Enrutamiento según confianza](https://docs.typesafe.ai/patterns/confidence-routing) | Separa la respuesta de la decisión de actuar y mide umbrales con datos propios. [Ver detalles](catalog/DETAILS.es.md#official-confidence-routing) |
| [Puntuación compuesta](https://docs.typesafe.ai/patterns/composite-scoring) | Evalúa dimensiones independientes y combínalas con pesos explícitos en el código. [Ver detalles](catalog/DETAILS.es.md#official-composite-scoring) |
| [Enrutamiento por intención](https://docs.typesafe.ai/patterns/intent-routing) | Clasifica solicitudes y dirígelas a reglas, modelos especializados o una persona. [Ver detalles](catalog/DETAILS.es.md#official-intent-routing) |
| [Asistente doméstico](https://docs.typesafe.ai/demos/smart-home) | Evalúa solicitudes de control del hogar con varias preguntas en una misma llamada. [Ver detalles](catalog/DETAILS.es.md#official-smart-home) |
| [Limitaciones conocidas de Jev 1.13](https://docs.typesafe.ai/model-jaggedness/jev-1.13) | Consulta debilidades y fallos documentados para esta versión concreta. [Ver detalles](catalog/DETAILS.es.md#official-jev-1-13) |
| [Consistencia de Noul](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) | Repite evaluaciones de reclamaciones para estudiar estabilidad e incertidumbre, no veracidad. [Ver detalles](catalog/DETAILS.es.md#official-consistency-noul-cookbook) |
| [Consistencia de Choice](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) | Añade una opción incierta a la moderación y compara concordancia y cobertura automática. [Ver detalles](catalog/DETAILS.es.md#official-consistency-choice-cookbook) |
| [Preguntas en paralelo](https://docs.typesafe.ai/cookbooks/parallel_questions) | Compara solicitudes agrupadas y separadas para varias preguntas sobre un documento. [Ver detalles](catalog/DETAILS.es.md#official-parallel-questions) |
| [Reordenación de resultados](https://docs.typesafe.ai/cookbooks/rerank_typesafe) | Reduce candidatos con BM25 y puntúa pares de consulta y pasaje; el ejemplo usa documentos jurídicos. [Ver detalles](catalog/DETAILS.es.md#official-rerank-typesafe) |
| [Búsqueda semántica por líneas](https://docs.typesafe.ai/cookbooks/semantic_find) | Selecciona líneas relevantes y comprueba por separado si existe una respuesta. [Ver detalles](catalog/DETAILS.es.md#official-semantic-find) |
| [Recuperación de estructura](https://docs.typesafe.ai/cookbooks/autoformat) | Clasifica saltos de línea, títulos, listas y bloques de código para reconstruir Markdown. [Ver detalles](catalog/DETAILS.es.md#official-autoformat) |
| [Llamadas a funciones con opciones limitadas](https://docs.typesafe.ai/cookbooks/function_calling) | Convierte nombres de funciones y argumentos finitos en decisiones tipadas. [Ver detalles](catalog/DETAILS.es.md#official-function-calling) |
| [Selección de habilidades](https://docs.typesafe.ai/cookbooks/skill_suggestion) | Ordena habilidades, examina una lista reducida y permite rechazar todos los candidatos. [Ver detalles](catalog/DETAILS.es.md#official-skill-suggestion) |
| [Correspondencia de entidades](https://docs.typesafe.ai/cookbooks/entity_alignment) | Decide si dos entidades deben fusionarse, mantenerse separadas o pasar a revisión humana. [Ver detalles](catalog/DETAILS.es.md#official-entity-alignment) |
| [Clasificación de pasajes RAG](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) | Comprueba relevancia, contradicciones e instrucciones inyectadas antes de generar la respuesta. [Ver detalles](catalog/DETAILS.es.md#official-classifying-rag-passages) |
| [Comprobación de citas](https://docs.typesafe.ai/cookbooks/citation_check) | Verifica que exista la cita y después evalúa si su contexto respalda la afirmación. [Ver detalles](catalog/DETAILS.es.md#official-citation-check) |
| [Controles de entrada y salida del LLM](https://docs.typesafe.ai/cookbooks/llm_guardrails) | Usa preguntas de riesgo y gravedad para aceptar, revisar o bloquear contenido. [Ver detalles](catalog/DETAILS.es.md#official-llm-guardrails) |
| [Extracción estructurada en cascada](https://docs.typesafe.ai/cookbooks/sde_cascade) | Extrae con un modelo pequeño, verifica campos con Jev y recurre a otro modelo cuando sea necesario. [Ver detalles](catalog/DETAILS.es.md#official-sde-cascade) |
| [Extracción de fechas](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) | Selecciona componentes de fechas; el código realiza los cálculos y la validación. [Ver detalles](catalog/DETAILS.es.md#official-date-extraction-cookbook) |
| [Extracción entre valores candidatos](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) | Encuentra candidatos con expresiones regulares, elige con Jev y copia el fragmento original. [Ver detalles](catalog/DETAILS.es.md#official-pre-parsed-value-extraction-cookbook) |
| [Clasificación jerárquica](https://docs.typesafe.ai/cookbooks/hierarchical_classification) | Recorre árboles de etiquetas con probabilidades y observa errores en ramas y hojas. [Ver detalles](catalog/DETAILS.es.md#official-hierarchical-classification) |
| [Descubrimiento automático de variables](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) | Un LLM propone preguntas, Jev genera variables numéricas y CatBoost aporta errores para iterar. [Ver detalles](catalog/DETAILS.es.md#official-autoresearch-feature-discovery) |
| [Clasificación con etiquetas más generales](https://docs.typesafe.ai/cookbooks/classification_using_confidence) | Clasifica informes anuales por sector y usa una categoría más amplia cuando la confianza es baja. [Ver detalles](catalog/DETAILS.es.md#official-classification-using-confidence) |

<a id="browser"></a>

## Navegador, escritorio y móvil

| Recurso | Resumen y detalles |
| --- | --- |
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Elige conjuntamente una acción del navegador y su destino en una tabla dinámica de elementos. [Ver detalles](catalog/DETAILS.es.md#browser-use--jev-ultrafast) |
| [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) | Lee la interfaz del Mac con OCR y accesibilidad; Jev elige la acción siguiente. [Ver detalles](catalog/DETAILS.es.md#awlevin--typesafe-computer-use) |
| [Jev Browser](https://github.com/jkudish/jev-browser) | Controla un navegador mediante biblioteca, CLI o MCP, con límites, recuperación y trazas. [Ver detalles](catalog/DETAILS.es.md#jkudish--jev-browser) |
| [Mobile Jev](https://github.com/droidrun/mobile-jev) | Selecciona acciones en un Android de Mobilerun a partir del estado de la interfaz. [Ver detalles](catalog/DETAILS.es.md#droidrun--mobile-jev) |
| [Unclutter](https://github.com/kitze/unclutter) | Detecta elementos superfluos de páginas y reutiliza reglas de plantilla en una extensión. [Ver detalles](catalog/DETAILS.es.md#kitze--unclutter) |
| [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock) | Clasifica elementos del DOM como anuncios y los elimina mediante código del navegador. [Ver detalles](catalog/DETAILS.es.md#realzachi--typesafe-adblock) |
| [Jev for Social Media](https://github.com/socai-io/jev-social) | Jev elige operaciones de redes sociales y socai las ejecuta en el navegador. [Ver detalles](catalog/DETAILS.es.md#socai-io--jev-social) |
| [Retriever AI: evaluación de un agente de navegador](https://rtrvr.ai/blog/jev-browser-agent-benchmark) | Informe del equipo sobre selección de acciones con Jev y planificación con GLM: más rapidez y mayor coste total. [Ver detalles](catalog/DETAILS.es.md#rtrvr-browser-benchmark) |

<a id="agents"></a>

## Agentes de programación y MCP

| Recurso | Resumen y detalles |
| --- | --- |
| [Typesafe MCP](https://github.com/itsmostafa/typesafe-mcp) | Ofrece decisiones tipadas de Jev a asistentes de programación mediante MCP. [Ver detalles](catalog/DETAILS.es.md#itsmostafa--typesafe-mcp) |
| [Jev MCP (jkudish)](https://github.com/jkudish/jev-mcp) | Herramientas MCP de verificación, filtrado, reclasificación y revisión de código. [Ver detalles](catalog/DETAILS.es.md#jkudish--jev-mcp) |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | Puntúa llamadas y resultados de herramientas, recorta contenido obsoleto y conserva el texto restante. [Ver detalles](catalog/DETAILS.es.md#tamaratran--fast-jev-compaction) |
| [Foreman](https://github.com/thruwire/foreman) | Evalúa si el trabajo está completo, suficientemente probado o necesita intervención humana. [Ver detalles](catalog/DETAILS.es.md#thruwire--foreman) |
| [Winnow](https://github.com/GhalebDweikat/winnow) | Filtra salidas extensas antes de incluirlas en el contexto y permite recuperar el texto oculto. [Ver detalles](catalog/DETAILS.es.md#ghalebdweikat--winnow) |
| [Jev Review (devagrawal09)](https://github.com/devagrawal09/jev-review) | Revisa cambios o repositorios por etapas: riesgos, selección de pruebas y gravedad. [Ver detalles](catalog/DETAILS.es.md#devagrawal09--jev-review) |
| [Jev Review MCP](https://github.com/NiazMorshed2007/jev-review) | Un servidor MCP local ofrece puntuaciones continuas de calidad a agentes de programación. [Ver detalles](catalog/DETAILS.es.md#niazmorshed2007--jev-review) |
| [Jev MCP (blakestone-x)](https://github.com/blakestone-x/jev-mcp) | Herramientas MCP y ejemplos para clasificar, puntuar, comparar y filtrar. [Ver detalles](catalog/DETAILS.es.md#blakestone-x--jev-mcp) |

<a id="routing"></a>

## Enrutamiento de modelos

| Recurso | Resumen y detalles |
| --- | --- |
| [Jev Codex Router](https://github.com/0xNatoshi/jev-codex-router) | Elige el modelo y la profundidad de razonamiento de cada turno mediante Jev. [Ver detalles](catalog/DETAILS.es.md#0xnatoshi--jev-codex-router) |
| [jev-router](https://github.com/gargpratyush/jev-router) | Dirige cada nuevo turno de Claude Code o Codex al nivel de modelo adecuado. [Ver detalles](catalog/DETAILS.es.md#gargpratyush--jev-router) |

<a id="safety"></a>

## Moderación, reglas y controles de seguridad

| Recurso | Resumen y detalles |
| --- | --- |
| [Tripwire](https://github.com/noelzappy/tripwire) | Comprueba respuestas antes de entregarlas, mediante middleware, proxy y políticas configurables. [Ver detalles](catalog/DETAILS.es.md#noelzappy--tripwire) |
| [jev-gates](https://github.com/rashedInt32/jev-gates) | Comprueba reglas, alcance y afirmaciones de finalización; eleva los casos que requieren revisión. [Ver detalles](catalog/DETAILS.es.md#rashedint32--jev-gates) |
| [pi-warden](https://github.com/DevMortimer/pi-warden) | Revisa cambios y herramientas frente a reglas, bucles de reintentos y pruebas de finalización. [Ver detalles](catalog/DETAILS.es.md#devmortimer--pi-warden) |
| [Safer with Jev](https://github.com/andrelandgraf/safer-with-jev) | Muestra evaluaciones de contenido combinadas con reenvío opcional de solicitudes HTTPS. [Ver detalles](catalog/DETAILS.es.md#andrelandgraf--safer-with-jev) |
| [Triagedy](https://github.com/m0rphtail/triagedy) | Convierte alertas de seguridad JSONL en decisiones tipadas dentro de una tubería Unix. [Ver detalles](catalog/DETAILS.es.md#m0rphtail--triagedy) |

<a id="retrieval"></a>

## Búsqueda y grafos de conocimiento

| Recurso | Resumen y detalles |
| --- | --- |
| [neo4jev](https://github.com/jexp/neo4jev) | Elige la siguiente relación del grafo y comprueba si se alcanzó la meta en una misma llamada. [Ver detalles](catalog/DETAILS.es.md#jexp--neo4jev) |

<a id="data"></a>

## Datos y observabilidad

| Recurso | Resumen y detalles |
| --- | --- |
| [pg-jev](https://github.com/realZachi/pg-jev) | Extensión de PostgreSQL para filtrar, ordenar y clasificar filas con condiciones en lenguaje natural. [Ver detalles](catalog/DETAILS.es.md#realzachi--pg-jev) |
| [jevQL](https://github.com/kylemclaren/jevql) | Añade evaluaciones de Jev en el cliente a consultas sobre PostgreSQL estándar. [Ver detalles](catalog/DETAILS.es.md#kylemclaren--jevql) |
| [duckdb-jev](https://github.com/colliber/duckdb-jev) | Devuelve decisiones tipadas sobre tablas o Parquet desde consultas DuckDB. [Ver detalles](catalog/DETAILS.es.md#colliber--duckdb-jev) |
| [Jev Logs](https://github.com/reachjalil/jevlogs) | Puntúa registros de OpenTelemetry antes de derivarlos a un análisis más costoso. [Ver detalles](catalog/DETAILS.es.md#reachjalil--jevlogs) |

<a id="automation"></a>

## Automatización cotidiana y hogar inteligente

| Recurso | Resumen y detalles |
| --- | --- |
| [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) | Evalúa el estado del hogar y devuelve valores para automatizaciones de Home Assistant. [Ver detalles](catalog/DETAILS.es.md#abovecolin--ha-jev) |
| [jev-shell-history](https://github.com/mrnugget/jev-shell-history) | Ordena comandos existentes del historial de zsh según lo que se está escribiendo. [Ver detalles](catalog/DETAILS.es.md#mrnugget--jev-shell-history) |

<a id="applications"></a>

## Aplicaciones y herramientas de contenido

| Recurso | Resumen y detalles |
| --- | --- |
| [TypeSafe AI Playground (Rust CLI)](https://github.com/markjaquith/typesafe-ai-playground) | Experimentos en un CLI de Rust: detección de datos privados, revisión de comentarios, tono y clasificación. [Ver detalles](catalog/DETAILS.es.md#markjaquith--typesafe-ai-playground) |
| [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) | Modera spam y enlaces fraudulentos en Discord con medidas progresivas. [Ver detalles](catalog/DETAILS.es.md#brainstormity--jev-moderation-bot) |
| [JEVMETER](https://github.com/ChetasLua/jevmeter) | Puntúa cada frase de una transcripción y muestra los resultados como un medidor en el vídeo. [Ver detalles](catalog/DETAILS.es.md#chetaslua--jevmeter) |
| [Kill My Idea](https://github.com/monteduro/killmyidea) | Evalúa una idea de negocio con preguntas paralelas y combina puntuaciones en un veredicto fijo. [Ver detalles](catalog/DETAILS.es.md#monteduro--killmyidea) |

<a id="games"></a>

## Juegos y simulaciones

| Recurso | Resumen y detalles |
| --- | --- |
| [1v1 Jev](https://github.com/emrickgarrett/OneVOneJev) | Una arena en el navegador usa Jev para elegir las acciones de un personaje. [Ver detalles](catalog/DETAILS.es.md#emrickgarrett--onevonejev) |
| [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) | Convierte RAM y telemetría del emulador en estado para elegir controles de NES. [Ver detalles](catalog/DETAILS.es.md#fhshaik--typesafe-mario) |
| [Jev Plays StarCraft](https://github.com/phyous/tsai-sc) | Controla una misión de StarCraft shareware desde estado estructurado y registra probabilidades. [Ver detalles](catalog/DETAILS.es.md#phyous--tsai-sc) |
| [Jev Pong](https://github.com/ably-labs/jev-pong) | Avanza la pelota de Pong un paso por decisión para visualizar la latencia. [Ver detalles](catalog/DETAILS.es.md#ably-labs--jev-pong) |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | Usa Jev para interpretar situaciones en una simulación de dron; el código se encarga del control rápido. [Ver detalles](catalog/DETAILS.es.md#romanslack--jev-drone) |
| [Jev Chess Lab](https://github.com/denikuchero/jev-chess-lab) | Experimentos de ajedrez comparan Jev solo, filtros tácticos y ayuda de Stockfish. [Ver detalles](catalog/DETAILS.es.md#denikuchero--jev-chess-lab) |

<a id="evaluation"></a>

## Evaluación y calibración

| Recurso | Resumen y detalles |
| --- | --- |
| [jevcal](https://github.com/abhixhek/jevcal) | Elige umbrales de confianza con datos propios y detecta cambios tras actualizar el modelo. [Ver detalles](catalog/DETAILS.es.md#abhixhek--jevcal) |
| [Janus](https://github.com/FirasSX914/Janus) | Mide cuándo derivar tareas entre modelos pequeños y grandes, y cuándo no conviene hacerlo. [Ver detalles](catalog/DETAILS.es.md#firassx914--janus) |
| [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) | Evalúa calibración de probabilidades, cobertura de automatización, latencia y consumo. [Ver detalles](catalog/DETAILS.es.md#abdelstark--jev-benchmarks) |
| [typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) | Compara la salida estructurada de un LLM con Jev en las mismas tareas. [Ver detalles](catalog/DETAILS.es.md#iammrduncan--typesafe-ai-benchmark) |
| [jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) | Usa una pregunta Noul para evaluar si fragmentos de código contienen credenciales utilizables. [Ver detalles](catalog/DETAILS.es.md#teyhouse--jev-secret-detection) |

<a id="experiments"></a>

## Experimentos con los límites

| Recurso | Resumen y detalles |
| --- | --- |
| [jev-llm](https://github.com/Code-Forge-AU/jev-llm) | Experimenta con generación de texto eligiendo repetidamente la siguiente palabra entre candidatos. [Ver detalles](catalog/DETAILS.es.md#code-forge-au--jev-llm) |

## Mantener el índice

La edición de referencia es la inglesa. Edita `data/resources.json`, actualiza las tres traducciones de `data/locales/` y genera todas las ediciones juntas. Requiere Python 3.10+, sin paquetes ni claves de API.

```sh
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/catalog.py --search browser --lang en
```

Se comprueban los datos, las traducciones completas, los duplicados, los archivos generados y los enlaces locales. No se verifica la disponibilidad remota ni se llama a modelos.

Consulta la [metodología](docs/METHODOLOGY.md), el [registro de investigación](docs/RESEARCH.md) y la [guía de contribución](CONTRIBUTING.md), en inglés. Las anotaciones y los scripts originales usan la [licencia MIT](LICENSE); los recursos enlazados conservan sus licencias.
