---
search:
  boost: 10.0
---

# Class: ThirdPartyRightsImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would affect the rights and freedoms of others_



<div data-search-exclude markdown="1">



URI: [justifications:ThirdPartyRightsImpaired](https://w3id.org/lmodel/dpv/justifications/ThirdPartyRightsImpaired)





```mermaid
 classDiagram
    class ThirdPartyRightsImpaired
    click ThirdPartyRightsImpaired href "../ThirdPartyRightsImpaired/"
      LegalProcessImpaired <|-- ThirdPartyRightsImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **ThirdPartyRightsImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ThirdPartyRightsImpaired](https://w3id.org/lmodel/dpv/justifications/ThirdPartyRightsImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Third Party Rights Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ThirdPartyRightsImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ThirdPartyRightsImpaired |
| native | justifications:ThirdPartyRightsImpaired |
| exact | dpv_justifications:ThirdPartyRightsImpaired, dpv_justifications_owl:ThirdPartyRightsImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ThirdPartyRightsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ThirdPartyRightsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would affect the rights and freedoms of others'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Third Party Rights Impaired
exact_mappings:
- dpv_justifications:ThirdPartyRightsImpaired
- dpv_justifications_owl:ThirdPartyRightsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:ThirdPartyRightsImpaired

```
</details>

### Induced

<details>
```yaml
name: ThirdPartyRightsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ThirdPartyRightsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would affect the rights and freedoms of others'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Third Party Rights Impaired
exact_mappings:
- dpv_justifications:ThirdPartyRightsImpaired
- dpv_justifications_owl:ThirdPartyRightsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:ThirdPartyRightsImpaired

```
</details></div>