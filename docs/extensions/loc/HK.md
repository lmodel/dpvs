---
search:
  boost: 10.0
---

# Class: HK 


_Concept representing Country of Hong Kong_



<div data-search-exclude markdown="1">



URI: [loc:HK](https://w3id.org/lmodel/dpv/loc/HK)





```mermaid
 classDiagram
    class HK
    click HK href "../HK/"
      CN <|-- HK
        click CN href "../CN/"
      
      
```





## Inheritance
* [CN](CN.md)
    * **HK**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HK](https://w3id.org/lmodel/dpv/loc/HK) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* China, Hong Kong Special Administrative Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HK |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HK |
| native | loc:HK |
| exact | dpv_loc:HK, dpv_loc_owl:HK, iso3166:HK |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Hong Kong
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- China, Hong Kong Special Administrative Region
exact_mappings:
- dpv_loc:HK
- dpv_loc_owl:HK
- iso3166:HK
is_a: CN
class_uri: loc:HK

```
</details>

### Induced

<details>
```yaml
name: HK
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HK
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Hong Kong
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- China, Hong Kong Special Administrative Region
exact_mappings:
- dpv_loc:HK
- dpv_loc_owl:HK
- iso3166:HK
is_a: CN
class_uri: loc:HK

```
</details></div>