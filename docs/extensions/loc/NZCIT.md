---
search:
  boost: 10.0
---

# Class: NZCIT 


_Concept representing region Chatham Islands in country New Zealand_



<div data-search-exclude markdown="1">



URI: [loc:NZ-CIT](https://w3id.org/lmodel/dpv/loc/NZ-CIT)





```mermaid
 classDiagram
    class NZCIT
    click NZCIT href "../NZCIT/"
      NZ <|-- NZCIT
        click NZ href "../NZ/"
      
      
```





## Inheritance
* [NZ](NZ.md)
    * **NZCIT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NZ-CIT](https://w3id.org/lmodel/dpv/loc/NZ-CIT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NZ-CIT
* Chatham Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NZ-CIT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NZ-CIT |
| native | loc:NZCIT |
| exact | dpv_loc:NZ-CIT, dpv_loc_owl:NZ-CIT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NZCIT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-CIT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Chatham Islands in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-CIT
- Chatham Islands
exact_mappings:
- dpv_loc:NZ-CIT
- dpv_loc_owl:NZ-CIT
is_a: NZ
class_uri: loc:NZ-CIT

```
</details>

### Induced

<details>
```yaml
name: NZCIT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NZ-CIT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Chatham Islands in country New Zealand
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NZ-CIT
- Chatham Islands
exact_mappings:
- dpv_loc:NZ-CIT
- dpv_loc_owl:NZ-CIT
is_a: NZ
class_uri: loc:NZ-CIT

```
</details></div>