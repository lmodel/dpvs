---
search:
  boost: 10.0
---

# Class: SS 


_Concept representing Country of South Sudan_



<div data-search-exclude markdown="1">



URI: [loc:SS](https://w3id.org/lmodel/dpv/loc/SS)





```mermaid
 classDiagram
    class SS
    click SS href "../SS/"
      SS <|-- SSEC
        click SSEC href "../SSEC/"
      SS <|-- SSJG
        click SSJG href "../SSJG/"
      SS <|-- SSNU
        click SSNU href "../SSNU/"
      
      
```





## Inheritance
* **SS**
    * [SSEC](SSEC.md)
    * [SSJG](SSJG.md)
    * [SSNU](SSNU.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SS](https://w3id.org/lmodel/dpv/loc/SS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* South Sudan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SS |
| native | loc:SS |
| exact | dpv_loc:SS, dpv_loc_owl:SS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of South Sudan
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- South Sudan
exact_mappings:
- dpv_loc:SS
- dpv_loc_owl:SS
class_uri: loc:SS

```
</details>

### Induced

<details>
```yaml
name: SS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of South Sudan
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- South Sudan
exact_mappings:
- dpv_loc:SS
- dpv_loc_owl:SS
class_uri: loc:SS

```
</details></div>