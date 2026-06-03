---
search:
  boost: 10.0
---

# Class: EGASN 


_Concept representing region Aswan Governorate in country Egypt_



<div data-search-exclude markdown="1">



URI: [loc:EG-ASN](https://w3id.org/lmodel/dpv/loc/EG-ASN)





```mermaid
 classDiagram
    class EGASN
    click EGASN href "../EGASN/"
      EG <|-- EGASN
        click EG href "../EG/"
      
      
```





## Inheritance
* [EG](EG.md)
    * **EGASN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:EG-ASN](https://w3id.org/lmodel/dpv/loc/EG-ASN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* EG-ASN
* Aswan Governorate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#EG-ASN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:EG-ASN |
| native | loc:EGASN |
| exact | dpv_loc:EG-ASN, dpv_loc_owl:EG-ASN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EGASN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-ASN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aswan Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-ASN
- Aswan Governorate
exact_mappings:
- dpv_loc:EG-ASN
- dpv_loc_owl:EG-ASN
is_a: EG
class_uri: loc:EG-ASN

```
</details>

### Induced

<details>
```yaml
name: EGASN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#EG-ASN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Aswan Governorate in country Egypt
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- EG-ASN
- Aswan Governorate
exact_mappings:
- dpv_loc:EG-ASN
- dpv_loc_owl:EG-ASN
is_a: EG
class_uri: loc:EG-ASN

```
</details></div>