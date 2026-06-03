---
search:
  boost: 10.0
---

# Class: PersonalDocuments 


_Information about and including personal documents e.g. diaries or_

_journals_



<div data-search-exclude markdown="1">



URI: [pd:PersonalDocuments](https://w3id.org/lmodel/dpv/pd/PersonalDocuments)





```mermaid
 classDiagram
    class PersonalDocuments
    click PersonalDocuments href "../PersonalDocuments/"
      External <|-- PersonalDocuments
        click External href "../External/"
      
      
```





## Inheritance
* [External](External.md)
    * **PersonalDocuments**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PersonalDocuments](https://w3id.org/lmodel/dpv/pd/PersonalDocuments) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Personal Documents




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PersonalDocuments |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PersonalDocuments |
| native | pd:PersonalDocuments |
| exact | dpv_pd:PersonalDocuments, dpv_pd_owl:PersonalDocuments |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonalDocuments
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PersonalDocuments
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about and including personal documents e.g. diaries or

  journals'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personal Documents
exact_mappings:
- dpv_pd:PersonalDocuments
- dpv_pd_owl:PersonalDocuments
is_a: External
class_uri: pd:PersonalDocuments

```
</details>

### Induced

<details>
```yaml
name: PersonalDocuments
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PersonalDocuments
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about and including personal documents e.g. diaries or

  journals'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Personal Documents
exact_mappings:
- dpv_pd:PersonalDocuments
- dpv_pd_owl:PersonalDocuments
is_a: External
class_uri: pd:PersonalDocuments

```
</details></div>