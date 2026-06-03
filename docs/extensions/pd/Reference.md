---
search:
  boost: 10.0
---

# Class: Reference 


_Information about references in the professional context_



<div data-search-exclude markdown="1">



URI: [pd:Reference](https://w3id.org/lmodel/dpv/pd/Reference)





```mermaid
 classDiagram
    class Reference
    click Reference href "../Reference/"
      Professional <|-- Reference
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **Reference**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Reference](https://w3id.org/lmodel/dpv/pd/Reference) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Reference




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Reference |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Reference |
| native | pd:Reference |
| exact | dpv_pd:Reference, dpv_pd_owl:Reference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Reference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Reference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about references in the professional context
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Reference
exact_mappings:
- dpv_pd:Reference
- dpv_pd_owl:Reference
is_a: Professional
class_uri: pd:Reference

```
</details>

### Induced

<details>
```yaml
name: Reference
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Reference
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about references in the professional context
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Reference
exact_mappings:
- dpv_pd:Reference
- dpv_pd_owl:Reference
is_a: Professional
class_uri: pd:Reference

```
</details></div>