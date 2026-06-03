---
search:
  boost: 10.0
---

# Class: DJ 


_Concept representing Country of Djibouti_



<div data-search-exclude markdown="1">



URI: [loc:DJ](https://w3id.org/lmodel/dpv/loc/DJ)





```mermaid
 classDiagram
    class DJ
    click DJ href "../DJ/"
      DJ <|-- DJAS
        click DJAS href "../DJAS/"
      DJ <|-- DJDI
        click DJDI href "../DJDI/"
      DJ <|-- DJDJ
        click DJDJ href "../DJDJ/"
      DJ <|-- DJOB
        click DJOB href "../DJOB/"
      DJ <|-- DJTA
        click DJTA href "../DJTA/"
      
      
```





## Inheritance
* **DJ**
    * [DJAS](DJAS.md)
    * [DJDI](DJDI.md)
    * [DJDJ](DJDJ.md)
    * [DJOB](DJOB.md)
    * [DJTA](DJTA.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DJ](https://w3id.org/lmodel/dpv/loc/DJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Djibouti




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DJ |
| native | loc:DJ |
| exact | dpv_loc:DJ, dpv_loc_owl:DJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Djibouti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Djibouti
exact_mappings:
- dpv_loc:DJ
- dpv_loc_owl:DJ
class_uri: loc:DJ

```
</details>

### Induced

<details>
```yaml
name: DJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Djibouti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Djibouti
exact_mappings:
- dpv_loc:DJ
- dpv_loc_owl:DJ
class_uri: loc:DJ

```
</details></div>