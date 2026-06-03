---
search:
  boost: 10.0
---

# Class: GBDUR 


_Concept representing region County Durham (district) in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DUR](https://w3id.org/lmodel/dpv/loc/GB-DUR)





```mermaid
 classDiagram
    class GBDUR
    click GBDUR href "../GBDUR/"
      GB <|-- GBDUR
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDUR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DUR](https://w3id.org/lmodel/dpv/loc/GB-DUR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DUR
* County Durham (district)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DUR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DUR |
| native | loc:GBDUR |
| exact | dpv_loc:GB-DUR, dpv_loc_owl:GB-DUR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDUR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DUR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region County Durham (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DUR
- County Durham (district)
exact_mappings:
- dpv_loc:GB-DUR
- dpv_loc_owl:GB-DUR
is_a: GB
class_uri: loc:GB-DUR

```
</details>

### Induced

<details>
```yaml
name: GBDUR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DUR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region County Durham (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DUR
- County Durham (district)
exact_mappings:
- dpv_loc:GB-DUR
- dpv_loc_owl:GB-DUR
is_a: GB
class_uri: loc:GB-DUR

```
</details></div>