---
search:
  boost: 10.0
---

# Class: CANS 


_Concept representing region Nova Scotia in country Canada_



<div data-search-exclude markdown="1">



URI: [loc:CA-NS](https://w3id.org/lmodel/dpv/loc/CA-NS)





```mermaid
 classDiagram
    class CANS
    click CANS href "../CANS/"
      CA <|-- CANS
        click CA href "../CA/"
      
      
```





## Inheritance
* [CA](CA.md)
    * **CANS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CA-NS](https://w3id.org/lmodel/dpv/loc/CA-NS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CA-NS
* Nova Scotia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CA-NS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CA-NS |
| native | loc:CANS |
| exact | dpv_loc:CA-NS, dpv_loc_owl:CA-NS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CANS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-NS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nova Scotia in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-NS
- Nova Scotia
exact_mappings:
- dpv_loc:CA-NS
- dpv_loc_owl:CA-NS
is_a: CA
class_uri: loc:CA-NS

```
</details>

### Induced

<details>
```yaml
name: CANS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CA-NS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nova Scotia in country Canada
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CA-NS
- Nova Scotia
exact_mappings:
- dpv_loc:CA-NS
- dpv_loc_owl:CA-NS
is_a: CA
class_uri: loc:CA-NS

```
</details></div>