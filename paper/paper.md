---
title: 'Trait MMAP: An upload-first mapper for mammal and parasite trait data'
tags:
  - biodiversity informatics
  - mammals
  - parasites
  - museum collections
  - GIS
authors:
  - name: Samuel C. Speck
    affiliation: 1
    corresponding: true
affiliations:
  - name: Kansas State University, United States
    index: 1
date: 17 September 2026
bibliography: paper.bib
---

# Summary
Trait MMAP (Mapper for Mammals and Parasites) is a browser-based research tool for rapidly exploring spatial and trait structure in biological datasets. Researchers upload a CSV, map coordinate and descriptive fields, identify arbitrary columns as numeric, categorical, or text traits, interactively filter and inspect records, select records spatially, and export analysis-ready subsets as CSV or GeoJSON.

# Statement of need
Biological collections and field projects increasingly combine geographic coordinates with taxonomic, morphological, life-history, host–parasite, and other trait information. Rapid exploratory mapping often requires researchers to restructure data for desktop GIS, write project-specific code, or adapt records to a fixed web portal. Trait MMAP provides a lightweight intermediate workflow in which researchers retain control of their tabular data while gaining interactive spatial filtering and selection.

[EXPAND WITH SPECIFIC USER AUDIENCE, RESEARCH PROBLEM, AND CITATIONS.]

# State of the field
[COMPARE WITH BIODIVERSITY PORTALS, COLLECTION DATABASES, GIS SOFTWARE, AND WEB-MAPPING TOOLS; EXPLAIN THE DISTINCT UPLOAD-FIRST NICHE.]

# Software design
Trait MMAP is a client-side Leaflet application. Core research data are uploaded and processed in the browser. Filtering is separated from visualization: a numeric field can be constrained by exact/minimum/maximum values independently of whether it sizes points. Categorical selections are strict, while inactive controls do not remove records with missing values. Spatial subsets can be defined by right-click, rectangle, or polygon selection and exported as CSV or GeoJSON. Optional reference services are separated from core upload/filter/export functions.

# Research impact statement
[ADD EVIDENCE OF ACTUAL USE: PROJECTS, USERS, DATASETS, PRESENTATIONS, MANUSCRIPTS, OR RESEARCH DECISIONS ENABLED BY TRAIT MMAP.]

# AI usage disclosure
Generative AI tools were used during software development and documentation drafting. AI-assisted code and text were iteratively reviewed, tested against controlled examples, and revised by the author. The author retained responsibility for software design decisions, scientific interpretation, validation, and final content.

[REVISE TO MATCH FINAL SUBMISSION AND JOURNAL POLICY.]

# Acknowledgements
[ADD ADVISOR/COLLABORATORS, COLLECTIONS, FUNDING, AND INSTITUTIONAL SUPPORT.]

# References
[ADD REFERENCES THROUGH paper.bib.]
