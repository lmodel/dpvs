---
search:
  boost: 10.0
---

# Class: BRSC 


_Concept representing region Santa Catarina in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-SC](https://w3id.org/lmodel/dpv/loc/BR-SC)





```mermaid
 classDiagram
    class BRSC
    click BRSC href "../BRSC/"
      BR <|-- BRSC
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRSC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-SC](https://w3id.org/lmodel/dpv/loc/BR-SC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-SC
* Santa Catarina




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-SC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-SC |
| native | loc:BRSC |
| exact | dpv_loc:BR-SC, dpv_loc_owl:BR-SC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRSC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santa Catarina in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-SC
- Santa Catarina
exact_mappings:
- dpv_loc:BR-SC
- dpv_loc_owl:BR-SC
is_a: BR
class_uri: loc:BR-SC

```
</details>

### Induced

<details>
```yaml
name: BRSC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santa Catarina in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-SC
- Santa Catarina
exact_mappings:
- dpv_loc:BR-SC
- dpv_loc_owl:BR-SC
is_a: BR
class_uri: loc:BR-SC

```
</details></div>