---
search:
  boost: 10.0
---

# Class: GBCMA 


_Concept representing region Cumbria in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-CMA](https://w3id.org/lmodel/dpv/loc/GB-CMA)





```mermaid
 classDiagram
    class GBCMA
    click GBCMA href "../GBCMA/"
      GB <|-- GBCMA
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBCMA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-CMA](https://w3id.org/lmodel/dpv/loc/GB-CMA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-CMA
* Cumbria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-CMA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-CMA |
| native | loc:GBCMA |
| exact | dpv_loc:GB-CMA, dpv_loc_owl:GB-CMA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBCMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CMA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Cumbria in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CMA
- Cumbria
exact_mappings:
- dpv_loc:GB-CMA
- dpv_loc_owl:GB-CMA
is_a: GB
class_uri: loc:GB-CMA

```
</details>

### Induced

<details>
```yaml
name: GBCMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-CMA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Cumbria in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-CMA
- Cumbria
exact_mappings:
- dpv_loc:GB-CMA
- dpv_loc_owl:GB-CMA
is_a: GB
class_uri: loc:GB-CMA

```
</details></div>