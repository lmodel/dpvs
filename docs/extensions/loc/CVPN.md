---
search:
  boost: 10.0
---

# Class: CVPN 


_Concept representing region Porto Novo (Cape Verde) in country Cabo_

_Verde_



<div data-search-exclude markdown="1">



URI: [loc:CV-PN](https://w3id.org/lmodel/dpv/loc/CV-PN)





```mermaid
 classDiagram
    class CVPN
    click CVPN href "../CVPN/"
      CV <|-- CVPN
        click CV href "../CV/"
      
      
```





## Inheritance
* [CV](CV.md)
    * **CVPN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CV-PN](https://w3id.org/lmodel/dpv/loc/CV-PN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CV-PN
* Porto Novo (Cape Verde)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CV-PN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CV-PN |
| native | loc:CVPN |
| exact | dpv_loc:CV-PN, dpv_loc_owl:CV-PN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CVPN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CV-PN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Porto Novo (Cape Verde) in country Cabo

  Verde'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CV-PN
- Porto Novo (Cape Verde)
exact_mappings:
- dpv_loc:CV-PN
- dpv_loc_owl:CV-PN
is_a: CV
class_uri: loc:CV-PN

```
</details>

### Induced

<details>
```yaml
name: CVPN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CV-PN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Porto Novo (Cape Verde) in country Cabo

  Verde'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CV-PN
- Porto Novo (Cape Verde)
exact_mappings:
- dpv_loc:CV-PN
- dpv_loc_owl:CV-PN
is_a: CV
class_uri: loc:CV-PN

```
</details></div>