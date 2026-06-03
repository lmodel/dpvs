---
search:
  boost: 10.0
---

# Class: BRGO 


_Concept representing region Goiás in country Brazil_



<div data-search-exclude markdown="1">



URI: [loc:BR-GO](https://w3id.org/lmodel/dpv/loc/BR-GO)





```mermaid
 classDiagram
    class BRGO
    click BRGO href "../BRGO/"
      BR <|-- BRGO
        click BR href "../BR/"
      
      
```





## Inheritance
* [BR](BR.md)
    * **BRGO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:BR-GO](https://w3id.org/lmodel/dpv/loc/BR-GO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* BR-GO
* Goiás




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#BR-GO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:BR-GO |
| native | loc:BRGO |
| exact | dpv_loc:BR-GO, dpv_loc_owl:BR-GO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BRGO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-GO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Goiás in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-GO
- Goiás
exact_mappings:
- dpv_loc:BR-GO
- dpv_loc_owl:BR-GO
is_a: BR
class_uri: loc:BR-GO

```
</details>

### Induced

<details>
```yaml
name: BRGO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#BR-GO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Goiás in country Brazil
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- BR-GO
- Goiás
exact_mappings:
- dpv_loc:BR-GO
- dpv_loc_owl:BR-GO
is_a: BR
class_uri: loc:BR-GO

```
</details></div>