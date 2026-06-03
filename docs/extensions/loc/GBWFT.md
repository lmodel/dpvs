---
search:
  boost: 10.0
---

# Class: GBWFT 


_Concept representing region London Borough of Waltham Forest in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-WFT](https://w3id.org/lmodel/dpv/loc/GB-WFT)





```mermaid
 classDiagram
    class GBWFT
    click GBWFT href "../GBWFT/"
      GB <|-- GBWFT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBWFT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-WFT](https://w3id.org/lmodel/dpv/loc/GB-WFT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-WFT
* London Borough of Waltham Forest




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-WFT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-WFT |
| native | loc:GBWFT |
| exact | dpv_loc:GB-WFT, dpv_loc_owl:GB-WFT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBWFT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WFT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Waltham Forest in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WFT
- London Borough of Waltham Forest
exact_mappings:
- dpv_loc:GB-WFT
- dpv_loc_owl:GB-WFT
is_a: GB
class_uri: loc:GB-WFT

```
</details>

### Induced

<details>
```yaml
name: GBWFT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-WFT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Waltham Forest in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-WFT
- London Borough of Waltham Forest
exact_mappings:
- dpv_loc:GB-WFT
- dpv_loc_owl:GB-WFT
is_a: GB
class_uri: loc:GB-WFT

```
</details></div>