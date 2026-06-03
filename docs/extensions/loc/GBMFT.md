---
search:
  boost: 10.0
---

# Class: GBMFT 


_Concept representing region Magherafelt (district) in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-MFT](https://w3id.org/lmodel/dpv/loc/GB-MFT)





```mermaid
 classDiagram
    class GBMFT
    click GBMFT href "../GBMFT/"
      GB <|-- GBMFT
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBMFT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-MFT](https://w3id.org/lmodel/dpv/loc/GB-MFT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-MFT
* Magherafelt (district)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-MFT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-MFT |
| native | loc:GBMFT |
| exact | dpv_loc:GB-MFT, dpv_loc_owl:GB-MFT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBMFT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MFT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Magherafelt (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MFT
- Magherafelt (district)
exact_mappings:
- dpv_loc:GB-MFT
- dpv_loc_owl:GB-MFT
is_a: GB
class_uri: loc:GB-MFT

```
</details>

### Induced

<details>
```yaml
name: GBMFT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-MFT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Magherafelt (district) in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-MFT
- Magherafelt (district)
exact_mappings:
- dpv_loc:GB-MFT
- dpv_loc_owl:GB-MFT
is_a: GB
class_uri: loc:GB-MFT

```
</details></div>