---
search:
  boost: 10.0
---

# Class: BI 


_Concept representing Country of Burundi_



<div data-search-exclude markdown="1">



URI: [loc:BI](https://w3id.org/lmodel/dpv/loc/BI)





```mermaid
 classDiagram
    class BI
    click BI href "../BI/"
      BI <|-- BIBB
        click BIBB href "../BIBB/"
      BI <|-- BIBM
        click BIBM href "../BIBM/"
      BI <|-- BIKI
        click BIKI href "../BIKI/"
      BI <|-- BIKR
        click BIKR href "../BIKR/"
      
      
```





## Inheritance
* **BI**
    * [BIBB](BIBB.md)
    * [BIBM](BIBM.md)
    * [BIKI](BIKI.md)
    * [BIKR](BIKR.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BI](https://w3id.org/lmodel/dpv/loc/BI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Burundi




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BI |
| native | loc:BI |
| exact | dpv_loc:BI, dpv_loc_owl:BI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Burundi
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Burundi
exact_mappings:
- dpv_loc:BI
- dpv_loc_owl:BI
class_uri: loc:BI

```
</details>

### Induced

<details>
```yaml
name: BI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Burundi
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Burundi
exact_mappings:
- dpv_loc:BI
- dpv_loc_owl:BI
class_uri: loc:BI

```
</details></div>