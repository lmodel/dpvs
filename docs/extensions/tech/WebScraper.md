---
search:
  boost: 10.0
---

# Class: WebScraper 


_Software that extracts data from websites to implement collection_

_practices colloquially called "web scraping"_



<div data-search-exclude markdown="1">



URI: [tech:WebScraper](https://w3id.org/lmodel/dpv/tech/WebScraper)





```mermaid
 classDiagram
    class WebScraper
    click WebScraper href "../WebScraper/"
      Software <|-- WebScraper
        click Software href "../Software/"
      
      
```





## Inheritance
* [Software](Software.md)
    * **WebScraper**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:WebScraper](https://w3id.org/lmodel/dpv/tech/WebScraper) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Web Scraper




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#WebScraper |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:WebScraper |
| native | tech:WebScraper |
| exact | dpv_tech:WebScraper, dpv_tech_owl:WebScraper |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WebScraper
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#WebScraper
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Software that extracts data from websites to implement collection

  practices colloquially called "web scraping"'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Web Scraper
exact_mappings:
- dpv_tech:WebScraper
- dpv_tech_owl:WebScraper
is_a: Software
class_uri: tech:WebScraper

```
</details>

### Induced

<details>
```yaml
name: WebScraper
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#WebScraper
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Software that extracts data from websites to implement collection

  practices colloquially called "web scraping"'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Web Scraper
exact_mappings:
- dpv_tech:WebScraper
- dpv_tech_owl:WebScraper
is_a: Software
class_uri: tech:WebScraper

```
</details></div>